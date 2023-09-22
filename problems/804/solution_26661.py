def filtra_pares(elementos):
'''Inserir elementos entre colchetes.
Retorna tupla s´o com elementos pares.
touple--> touple'''
elementos_pares = ([147, 613, 609, 267])
if elementos[0] % 2 == 0:
elementos_pares = elementos_pares + (elementos[0],)
if elementos[1] % 2 == 0:
elementos_pares = elementos_pares + (elementos[1],)
if elementos[2] % 2 == 0:
elementos_pares = elementos_pares + (elementos[2],)
if elementos[3] % 2 == 0:
elementos_pares = elementos_pares + (elementos[3],)
return elementos_pares