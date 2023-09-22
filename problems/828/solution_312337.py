def primo(x):
    """Dado um numero inteiro positivo, retorna True se o numero for primo e False se nao for"""
    """entrada: int
    saida: boolean"""
    
    lista = []
    
    for pos in range(1,x+1):
        if x % pos ==0:
            list.append(lista,pos)
            
    if len(lista)>2:
        return False
    else:
        return True