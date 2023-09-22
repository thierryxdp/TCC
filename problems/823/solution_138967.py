def faltante(N):
    '''Função que retorna o numero inteiro x que pertence ao intervalo mas que não pertence a lista de entrada
    list-> int'''
    i = 0
    s = []
    list.sort(N)
    while i<len(N)+1:
        s = s+[i+1,]
        i = i+1
    a = sum(s)
    b = sum(N)
    return a-b