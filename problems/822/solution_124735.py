def repetidos(lista):
    'dado uma lista de numeros, retorna o numero de vezes que um elemento é igual ao anterior'
    contador=1
    repetidos=0
    while contador<len(lista):
        if lista[contador] == lista[contador-1]:
            repetidos += 1
        contador += 1
    return repetidos