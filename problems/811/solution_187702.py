# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas: list[int], h: int, l:int) -> bool:
    '''Recebe dimenções do colchão, a altura da porta e largura da porta. Retorna se é possível
    passar com o colchão pela porta'''
    #Preparando variáveis
    retorno = False
    a = medidas [0]
    b = medidas [1]
    c = medidas [2]

    #Situação 1
    if(a < l and b < h):
        retorno = True
    #Situação 2
    elif (a < l and c < h):
        retorno = True
    elif (b < l and c < h):
        retorno = True
    elif (b <l and a < h):
        retorno = True
    elif (c < l and a <h):
        retorno = True
        
    return retorno