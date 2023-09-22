def faltante(L:list)->int:
    """ A função recebe como parâmetro de entrada uma lista L de tmanho N-1 contendo números inteiros(não repetidos) de 1 a N. E deve retornar o número inteiro x, que pertence a lista L"""  
    Lcompleta = list(range(L[0],L[-1]+1))
    indice = 0
    resposta = 0
    if len(L) != len(Lcompleta):
        while indice < len(L):
            if L[indice] != L[indice]:
                resposta = L[indice] - 1
                indice = indice + 1
    else:
        resposta = resposta + (L[-1] + 1)
    return resposta