def faltante (N):
    '''Função que retorna o número inteiro x que pertence ao intervalo mas que não pertence a lista de entrada n, dado como entrada a lista ordenada N
    list -> int'''
   	i = 0
    s= []
    list.sort(N)
    while i<len(N)+1:
        s = s+1
    return sum(s)-sum(N)