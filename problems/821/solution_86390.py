#QUESTÃO5
def fatorial (numero):
    '''
    Retorna o fatorial do
    numero inserido.
    int -> int
    '''
    produto = 1
    vezes = 1
    while vezes <= numero:
        produto = produto*(vezes)
        vezes = vezes+1
    return produto