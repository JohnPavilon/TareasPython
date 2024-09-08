import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime

# Función para obtener el MD5 y SHA1 de un archivo
def calcular_hash(archivo):
    hash_md5 = hashlib.md5()
    hash_sha1 = hashlib.sha1()

    with open(archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_md5.update(bloque)
            hash_sha1.update(bloque)
    return hash_md5.hexdigest(), hash_sha1.hexdigest()

# Función para general el reporte
def generar_reporte(xml_file):
    # Obtener hora de ejecución y lo convertimos a formato dd/mm/aaaa HH:MM:SS 
    hora_ejecucion = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Calcular MD5 y SHA1 del archivo XML llamando a nuestra anterior función
    md5_hash, sha1_hash = calcular_hash(xml_file)

    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Inicializamos contadores
    hosts_prendidos = 0
    hosts_apagados = 0
    puerto_22 = 0
    puerto_53 = 0
    puerto_80 = 0
    puerto_443 = 0
    hosts_con_dominio = 0
    servidores_http = set() # Set es para registrar todos los servidores http sin repetir
    apache_count = 0
    nginx_count = 0
    honeypots_dionaea = 0

    # Recorrer los hosts en el archivo XML, lo que hacemos es buscar la etiqueta especificada, el atributo deseao y ver
    # si cumple con estar en x estado, en caso de que se cumpla le sumamos 1 a su respectivo contador
    for host in root.findall('host'):
        estado = host.find("status").attrib["state"]
        if estado == "up":
            hosts_prendidos += 1
        else:
            hosts_apagados += 1

        # Revisar puertos abiertos
        for puerto in host.findall("ports/port"):
            port_id = puerto.attrib["portid"]
            estado_puerto = puerto.find("state").attrib["state"]
            
            if estado_puerto == "open":
                if port_id == "22":
                    puerto_22 += 1
                elif port_id == "53":
                    puerto_53 += 1
                elif port_id == "80":
                    puerto_80 += 1
                elif port_id == "443":
                    puerto_443 += 1

            # Revisar el tipo de servicio
            service = puerto.find("service")
            if service is not None:
                nombre_servicio = service.attrib.get("name", "")
                producto_servicio = service.attrib.get("product", "")

                # Verificar si es un servidor HTTP
                if "http" in nombre_servicio:
                    servidores_http.add(producto_servicio)  # Agregamos el servidor HTTP detectado a la lista
                    if "Apache httpd" in producto_servicio:
                        apache_count += 1
                    if "nginx" in producto_servicio:
                        nginx_count += 1

                # Verificar si es servidor con dominio
                if "domain" in nombre_servicio:
                    hosts_con_dominio += 1

                # Verificar si es un honeypot (Dionaea)
                if "Dionaea Honeypot httpd" in producto_servicio:
                    honeypots_dionaea += 1

    # Reporte
    reporte = (
        f"Hora de ejecución: {hora_ejecucion}\n"
        f"MD5 del archivo XML: {md5_hash}\n"
        f"SHA1 del archivo XML: {sha1_hash}\n"
        f"Hosts prendidos: {hosts_prendidos}\n"
        f"Hosts apagados: {hosts_apagados}\n"
        f"Hosts con puerto 22 abierto: {puerto_22}\n"
        f"Hosts con puerto 53 abierto: {puerto_53}\n"
        f"Hosts con puerto 80 abierto: {puerto_80}\n"
        f"Hosts con puerto 443 abierto: {puerto_443}\n"
        f"Hosts con nombre de dominio: {hosts_con_dominio}\n"
        f"Servidores HTTP detectados: {', '.join(servidores_http)}\n"
        f"Hosts que usan Apache: {apache_count}\n"
        f"Hosts que usan Nginx: {nginx_count}\n"
        f"Honeypots Dionaea detectados: {honeypots_dionaea}\n"
    )

    # Imprimimos en consola
    print(reporte)

    # Escribir el reporte en un archivo txt
    with open("reporte.txt", "w") as f:
        f.write(reporte)

xml_file = "nmap.xml" 
generar_reporte(xml_file)
