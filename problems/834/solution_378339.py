def media_matriz(M):
    """retorna a media de todos os numeros da matriz M;
    list(list) -> float"""
    soma=0
    i=0
    elem=0
    for n in M:
        for x in M[i]:
        	soma=soma+x
            elem=elem+1
        i=i+1
    
    return round(soma/elem,2)