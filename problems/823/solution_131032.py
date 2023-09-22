def peca_perdida(lista):
    ''' Função que recebe uma lista de inteiros de 1 a N com um elemento faltando,
retorna o elemento que esta faltando.
list -> int
'''
    for i in range(1,len(lista)+1):
        if i not in lista:
            return i