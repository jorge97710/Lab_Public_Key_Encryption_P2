# Cristina Bautista 161260
# Abril Palencia 18198
# César Rodas 16776
# Jorge Azmitia 15202
# 161260
# Parte 2 - Implementacion 
# Ejercicio 1
# Algoritmo ElGamal desde 0

import random
from math import pow

# funciones vistas en clase 

# a**b mod c
def power(a, b, c): 
  x = 1
  y = a 
  while b > 0: 
    if b % 2 == 0: 
      x = (x * y) % c; 
    y = (y * y) % c 
    b = int(b / 2) 
  return x % c 

def gcd(a, b): 
  if a < b: 
    return gcd(b, a) 
  elif a % b == 0: 
    return b; 
  else: 
    return gcd(b, a % b)

def gen_key(q): 
  key = random.randint(pow(5, 10), q) 
  while gcd(q, key) != 1: 
    key = random.randint(pow(5, 10), q) 
  return key 

def my_function_cipher(v, list_message):
  list_nums_cphr = []
  for i in range(len(list_message)): 
    each_list_nums_cphr = v * text_number[i]
    list_nums_cphr.append(each_list_nums_cphr)
  return list_nums_cphr


def my_function_decipher(v, list_message_cipher):
  decipher_nums = []
  for i in range(len(list_message_cipher)): 
    decipher_nums.append(int(list_message_cipher[i]/v))
  return decipher_nums

def encrypt(message, q, h, g):
  b = gen_key(q)
  u = power(g, b, q)
  v = power(h, b, q)

  print('b (gcd(b, q) = 1):', b)
  print('u (g**b mod q):', u)
  print('v (h**b mod q = g**ab mod q):', v)

  ciphertext = my_function_cipher(v, message)
  return u, ciphertext

def decrypt(c, u, a, q): 
  decipher_message = [] 
  v = power(u, a, q)  # u**a mod q = g**ba mod q
  decipher_message = my_function_decipher(v, c)   
  return decipher_message 


g = random.randint(pow(5, 10), pow(5, 20))
q = random.randint(2, g)
a = gen_key(q)
h = power(g, a, q)

print("g: ", g)
print("q: ", q)
print("a: ", a)
print("h o g**a: ", h)
  
# Este b deberia ser generado como en DH
b = gen_key(q) # gcd(b, q) = 1.
u = power(g, b, q) # g**b mod q
v = power(h, b, q) # h**b mod q



abecedario = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 
							11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
							21: 't', 22: 'u', 23: 'v', 24: 'w', 25: 'x', 26: 'y', 27: 'z'}

# el mensaje es lero lero en numeros
text_number = [12, 5, 18, 15, 12, 5, 18, 15]
print("Mensaje original: ", text_number)

u, c = encrypt(text_number, q, h, g)
print("Mensaje encriptado: ", c)

decrypt_message = decrypt(c, u, a, q)

print("Mensaje desencriptado: ",decrypt_message)

def traducir(text):
  texto = []
  # en este for busca cada numero la letra que le corresponde
  # para mostrar el texto
  for number in decrypt_message:
    letter = abecedario[number]
    texto.append(letter)
  return texto

print("Mensaje traducido: ", traducir(decrypt_message))