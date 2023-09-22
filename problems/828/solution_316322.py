def primo(valor):
    """
    Ao inserir um valor, o código retornará 
    true or false para número primo. 
    int->bool
    """
    cont=0
    for c in range(1,valor+1):
        if valor%c==0:
            cont+=1
    if cont==2:
        return True
    else:
        return False