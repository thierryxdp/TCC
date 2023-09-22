def fatorial(numero):
    ''' função que retorna o valor do fatorial do número fornecido
        [int-->int]'''

    ordem = list(range(numero+1))
    indice = 0
    fatorial = numero
    list.remove(ordem,0)

    while len(ordem) > indice :
         X = ordem[indice]
         fatorial *= X
    indice += 1
    return fatorial