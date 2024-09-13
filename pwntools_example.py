from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def rot13(cadena):
    return ''.join[chr((ord(x)+13)%26+97) for x in cadena]

def decode(type_enc, encoded):
    if type_enc == 'rot13':
        decoded = rot13(encoded)
    return decoded

received = json_recv()

print("Received type: ")
if received["type"] == 'rot13':
    decode('rot13', received["encoded"])
print()
print("Received encoded value: ")
print(received["encoded"])

to_send = {
    "decoded": "changeme"
}
json_send(to_send)

json_recv()
