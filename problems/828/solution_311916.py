def primo(n):
    """esta função diz se o numero n é primo
    int->bool"""
    if n>=2:
        lista=[]
        for numero in range(n):
            if numero==0:
                lista=[]
            else:
                if n%numero==0:
                    list.append(lista,numero)
                    a=len(lista)
                    if a<=2:
                        return True
            else:
                return False