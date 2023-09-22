def repetidos(x):
    """Função que recebe uma lista e retorna quantas vezes o número anterior é igual ao atual"""
    """list--->int"""
    resposta=0
    i=0
    while i<len(x):
        if x[i]==x[i-1]:
            resposta+=1
     	i+=1
    return resposta