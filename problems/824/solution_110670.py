def uppCons(frase):
    ''' funcao que recebe como entrada uma frase e retorna a frase com 
    suas consoantes em caixa alta 
    str -> str '''
    palavras = ''
    for consoante in frase:
        if consoante in 'b,c,ç,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z':
            palavras += consoante.upper()
        else:
            palavras += consoante
    return palavras