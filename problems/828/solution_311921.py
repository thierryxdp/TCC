def primo(n):
    """esta função diz se o numero n é primo
    int->bool"""
    if n>=2:
        lista=[]
        for numero in range(n):
            if numero==0:
                lista=[]
            elif n%numero==0:
                    list.append(lista,numero)
                    a=len(lista)
                    if a>2:
                        return False
            else:
                return True