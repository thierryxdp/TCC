def posLetra(x,l,n):
    """Função que retorna em qual posição esta a n ocorrência da letra indicada em 'l'"""
    """str-->int"""
    i=0
    while i<n:
        p=str.find(x,l)
        x=x[p:]
        i+=1
        
    return p