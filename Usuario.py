import hashlib

class Usuario:
    def __init__(self, nombre, email, password_hash):
        self.nombre = nombre
        self.email = email
        self.password_hash = password_hash 

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, email={self.email}, password_hash={self.password_hash})"

    def set_nombre(self, name):
        self.nombre = name

    def get_nombre(self):
        return self.nombre
    
    def set_password(self, pwd):
        # Guardar el hash de la nueva contraseña
        self.password_hash = hashlib.sha256(pwd.encode()).hexdigest()

    def get_password_hash(self):
        # Devuelve el hash de la contraseña
        return self.password_hash
    
    def is_password(self, pwd):
        # Compara el hash de la contraseña ingresada con el hash almacenado
        return hashlib.sha256(pwd.encode()).hexdigest() == self.get_password_hash()
    
    def set_email(self, mail):
        self.email = mail

    def get_email(self):
        return self.email