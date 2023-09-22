def primo(x):
    """retorna se um número é primo ou não
    int->bool"""
    if x>=2:
        lista=[]
        for n in range(x):
            if n==0:
                lista=[]
            elif x%n==0:
                list.append(lista,n)
        if len(lista)>1:
            return False
        else:
            return True