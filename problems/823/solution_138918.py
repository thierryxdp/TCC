def faltante(N):
    ''' Função que retorna o número inteiro x que pertence ao intervalo mas que não pertence a lista de entrada n, dado como entrada a lista ordenada N
    list -> int '''
    i = 0
    s = []
    list.sort(N)
    while i<len(N)+1:
        s = s+[i+1,]
        i = i+1
    a = sum(s)
    b = sum(N)
    return a-b