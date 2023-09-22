def primo(numero):
    """verifica se um numero é primo ou não:int->bool"""
    x=1
    lista=[]
    while x<=numero:
        if numero%x==0:
            list.append(lista,x)
        x=x+1
    if len(lista)<=2:
        return True
    else:
        return False