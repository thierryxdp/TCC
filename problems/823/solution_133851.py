def faltante(L):
    '''
    list -----> int
    funcao recebe lista dos n primeiros numeros, sendo qeu falta um
    ela retorna esse um que falta
    '''
    i = 1
      
    
    while i<=len(L)+1:
       n_numeros += [i]
       i+=1
    
    k = 0
    while k < len(L):
        if L[k] in n_numeros:
            index = n_numeros.index(L[k])
            n_numeros.pop(index)
        k+=1
        
        
    return n_numeros[0]