def repetidos(lista):
    """Em construção"""
contador = 0
soma = 0
while contador < len(lista):
    caracter = lista[contador]
    caracterant = lista[contador - 1]
    if caracter == caracterant:
        soma += 1
    contador +=1
return soma