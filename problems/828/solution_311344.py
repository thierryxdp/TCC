def primo(n):
    """Dado um número inteiro como entrada, retorna o booleano True se 
    este for primo ou False, caso contrário.
    int->bool"""
    lista=[]
    for num in range(1,n+1):
        if n%num==0:
            lista.append(num)
    if lista[0]==1 and lista[1]==n:
        return True
    else:
        return False