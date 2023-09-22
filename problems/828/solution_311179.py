def primo (x):
    """Função que dado um numero inteiro positivo, verifica se é primo ou não.
        int -> bool"""
    lista=[]
    for i in range(1,x+1):
        if x%i==0:
            lista=lista+[i]
    if len(lista)==2:
        return True
    else:
        return False