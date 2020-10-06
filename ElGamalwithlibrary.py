'''Sebastián Maldonado 18003
Cristina Bautista 161260
Abril Palencia 18198
César Rodas 16776
Jorge Azmitia 15202

La librería utilizada para el metodo de ElGamal es elgamal.py extraída de https://github.com/RyanRiddle/elgamal'''

import elgamal

print("\nPrimero se generan las llaves privada y publica en un diccionario")
llaves=elgamal.generate_keys()
publica=llaves["publicKey"]
privada=llaves["privateKey"]

mensaje="Este es el mensaje que será encriptado"
print("\nSe crea el mensaje a encriptar, el cual será: '"+mensaje+"'")
cipher=elgamal.encrypt(publica,mensaje)
print("Se encripta y se obtiene el ciphertext:",cipher)
plain=elgamal.decrypt(privada,cipher)
print("\nFinalmente se desencripta el mensaje y se obtiene:",plain)
