def faltante(L):
    """Funcao recebe uma lista: L de tamanhao [1,N] composta com numeros
    inteiros nao repetidos e retorna qual numero pertence ao intervalo da
    lista e esta faltando """

    L.sort()
    
    contador = 1
    
    if L[0] != 1:
        return 1
    else:
        while contador < len(L):
            if L[contador] == L[-1]:
                return L[contador]+1
            elif L[contador] == L[contador-1]+1:
                contador += 1
            else:
                return L[contador]-1