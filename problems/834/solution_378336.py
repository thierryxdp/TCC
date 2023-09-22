def media_matriz(M):
    """retorna a media de todos os numeros da matriz M;
    list(list) -> float"""
    soma=0
    i=0
    for n in M:
        for x in M[i]:
        	soma=soma+x
        i=i+1
        
    elem=0
    for y in M:
        for z in M[elem]:
            elem=elem+1
    
    return soma/elem