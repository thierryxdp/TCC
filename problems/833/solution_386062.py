def conta_numero(m,n):
    '''Funcao recebe uma matriz m de tamanho quaalquer e um numero tambem qualquer e retorna quantas vezes esse numero se repete nessa matriz
list, int -> int'''
    contador = 0
    for i in m:
        for b in i:
            if (b==n):
                contador += 1
    return contador