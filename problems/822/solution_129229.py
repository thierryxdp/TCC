def repetidos(lista):
    '''funçao dado uma lista de numero retorna quantas vezes o elemento é igual ao anterior
    list -> int'''
    repetido = 0
    contador = 0
    while contador < len(lista):
        if lista[contador] == lista[contador-1]:
            repetido += 1
            contador += 1
        else:
            contador += 1
    return repetido