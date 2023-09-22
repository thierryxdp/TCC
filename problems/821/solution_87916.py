def fatorial(n):
    ''' Função que retorna a fatorial de um dado número n 
    int -> int '''
    i = 1
    resposta = n
    while (n-i) != 0:
        resposta = resposta*(n-i)
        i = i+1
    return resposta