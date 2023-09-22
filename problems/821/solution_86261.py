def fatorial(num):
    '''
        Função que retorna o fatorial do número indicado;
        int => int 
    '''
    i = 1
    for num in range(2, num + 1):
        i = i * num
    return(i)