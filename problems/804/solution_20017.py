def filtra_pares(t):
    """retorne uma tupla contendo somente os números pares da tupla de entrada"""
    lista=[]
    if type(t)==tuple and len(t)==4:
        for p in t:
            if type(p)!=int:
                list=[]
                return('todos os elemntos da tupla devem ser ineteiros')
                break
                elif (p%2==0):
                    lista.append(p)
                    return (tuple(lista))
                else:
                    return ('Apenas será aceito uma tupla com 4 elementos')