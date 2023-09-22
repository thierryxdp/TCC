def faltante(lista):
    '''Retorna o número da peça que está faltando do quebra-cabeça;
       list -> int'''
    lista.sort()
    if lista[0] != 1:
        return 1
    else:
        contador = 0
        while lista[contador+1] - lista[contador] == 1:
            contador = contador + 1
        return contador + 2