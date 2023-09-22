def faltante(lista):
    '''Função que recebe uma lista de números inteiros não repetidos em um intervalo de
    1 a N e retorna o número que está faltando neste intervalo; list - > int'''
  
    lista.sort()
    cont = 0

    while cont < len(lista):
        if lista[cont] != cont+1:
            return cont+1
        elif cont == len(lista):
            return cont+2
        else:
            cont += 1