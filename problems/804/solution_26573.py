def filtra_pares (t):
    tupla=()
    if type(t)==tuple and len (t)==4:
        for i in t:
            if type (i)!=int:
                tupla=()
                print ('todos os intes devem ser inteiros.')
                break
            elif i%2==0:
                tupla.append(i)
       print(tuple(tupla))
    else:
        print('apenas sera aceito, uma tupla, com quatro intens')