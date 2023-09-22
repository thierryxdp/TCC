def fatorial (numero):
    '''Função que retorna o valor do fatorial do número fornecido;
    int->int'''
    
    ordem = list(range(numero +1))
    i = 0
    fatorial = 1
    list.remove(ordem,0)
    
    while len(ordem) > i:
        x = ordem[i]
        fatorial *= x
        indice += 1
    return fatorial