'''Função que recebe uma lista de números e retorna o número de vezes que um
elemento da lista é igual ao elemento anterior'''
'''list(floats) --> int'''
def repetidos(lista):
    contador=0
    aux=0
    for n in lista:
        contador += 1
        if contador < len(lista):
            if n == lista[contador]:
                aux +=1
    return aux