from scapy.all import *

def escanear_puerto_syn(ip, puertos):
    estado = []
    for port in puertos:
        paquete = IP(dst=ip)/TCP(dport=port, flags="S")
        respuesta = sr1(paquete, timeout=1, verbose=0)
        if respuesta is None:
            estado.append("Filtrado")
        elif respuesta.haslayer(TCP):
            if respuesta.getlayer(TCP).flags == 0x12: # SYN-ACK
                send(IP(dst=ip)/TCP(dport=port, flags="R"), verbose=0)
                estado.append("Abierto")
            elif respuesta.getlayer(TCP).flags == 0x14: # RST-ACK
                estado.append("Cerrado")
        else:
            estado.append("Desconocido")
    return estado

puertos = [22, 80, 170, 8080]
estados = escanear_puerto_syn('127.0.0.1',puertos)
for port in puertos:
    print(f'\nEstado del puerto {port}: {estados[puertos.index(port)]}')
    
