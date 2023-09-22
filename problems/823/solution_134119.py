def faltante(lista):
    '''Retorna o número da peça que está faltando do quebra-cabeça;
       list -> int'''
    lista.sort()
    soma_pontas = len(lista)+2
    contador = 0
    while contador < 1 + len(lista)//2:
        if lista[contador] + lista[-1*(contador+1)] == soma_pontas:
            contador = contador + 1
        elif lista[contador] != contador + 1:
            return contador + 1
        else:
            return lista[-1*(contador+1)] + 1
    return len(lista)/2