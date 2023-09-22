def posLetra(texto,letra,n):
    '''Dado uma texto, uma letra e um número n que representa a
    ocorrência desejada da letra, retorna a posição da ocorrência
    n da letra no texto. Caso exista menos ocorrencias que n,
    no texto, retorna -1.
    str, str, int -> int'''
    cont=0
    ocor=1
    while cont < len(texto):
        if texto[cont] == letra:
            if ocor == n:
                return cont
            else: 
                ocor = ocor+1
        cont = cont+1
    return -1