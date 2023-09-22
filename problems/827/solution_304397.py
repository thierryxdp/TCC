def qtd_divisores(x):
    """Dado um numero, retorna a quantidade de divisores que esse numero possui"""
    """entrada: int
    saida: int"""
    
    lista = []
    
    for pos in range(1,x+1):
        if x % pos ==0:
            list.append(lista,pos)
    
    return len(lista)