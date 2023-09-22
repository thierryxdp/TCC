def primo(n):
    qtd=0
    for numero in range(2,n):
        if n%numero==0:
            qtd+=1
    if qtd!=0:
        return False
    else:
        return True