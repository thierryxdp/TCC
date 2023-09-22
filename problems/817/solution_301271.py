def maiores(lis,n):
    """Função que insere um número 'n' numa lista 'lis' e devolve uma outra lista com os valores maiores que 'n'.
assinatura: list, int -> list
"""
    adc= list.append(lis,n)
    org= list.sort(lis)
    ind= list.index(lis,n)
    nli= lis[ind+1::1]
    return nli

def acima_da_media(lis)