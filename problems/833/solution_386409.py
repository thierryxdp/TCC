def conta_numero(n,m):
    """dado um numero inteiro e uma matriz conta e retorna quantas vezes aquele numero aparece
	int,list->"""
    
    soma = 0
    
    for i in m:
        if i in m:
            soma = soma + list.count(i,n)
    return soma