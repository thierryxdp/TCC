def filtra_pares (t):
    tupla=()
    if type(t)==tuple and len (t)==4:
        for i in t:
            if type (i)!=int:
                tupla=()
                return ('todos os intes devem ser inteiros.')
                break
            elif i%2==0:
                tupla.append(i)
       return(tuple(tupla))
    else:
        return('apenas sera aceito, uma tupla, com quatro intens')