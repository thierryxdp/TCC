def uppCons(frase):
    '''Recebe uma frase a analisa o parâmetro de entrada e retorna todas 
    as consoantes encontradas em maiúsculas e os demais caractéres no formato original
    tupla -> tupla'''
    
    consoantes = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'
    i = 0
    lista = ''
    while i < len(frase):
        if frase[i] in consoantes:
            novo = frase[i].upper()
            lista = lista + novo
        else:
            lista = lista + novo
        i = i + 1
    
    return lista