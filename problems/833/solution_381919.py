def conta_numero(n,m):
    '''Função que retorna quantas vezes um número inteiro n aparece numa matriz m de números inteiros
    list[list], int -> int'''
    qtd=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j==n:
                qtd+=1
    return qtd