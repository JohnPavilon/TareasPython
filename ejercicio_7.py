import re

nombres = r'[A-Z][a-z]+\s[A-Z][a-z]+'
resultado = re.findall(nombres, "Jonathan Valencia")

twitter = r'@\w+'
user = re.findall(twitter, "@usuario123 @otro_usuario @")

anycase = r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$'
text = re.findall(anycase, "H0l4")

print(resultado)
print(user)
print(text)