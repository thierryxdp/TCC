def uppCons(frase):
    """A função retorna todas as suas consoantes em maiúsculas e
    os demais caracteres exatamente como estavam na frase original.
    str-->str."""
    i = 0
    lista_frase = list(frase)
    consoantes = [b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z]
    while i < len(lista_frase):
        if lista_frase[i] in consoantes:
            list.insert(lista_frase,i,lista_frase[i].upper())
            i +=1
    return lista_frase