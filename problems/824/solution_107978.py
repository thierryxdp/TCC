def uppCons(frase):
    """Retorna a frase com todas as consoantes em maiúsculas.
    Paramtros:
    Entrada:str
    Saida:str"""
    lista=list(frase)
    cosoantes=""
    i=0
    while i<len(frase):
        if lista[i] in "h,b,c,d,f,g,j,k,ç,l,m,n,p,q,r,s,t,v,w,x,z":  
        	lista[i]=str.upper(lista[i])
        i=i+1
    return str.join("",lista)