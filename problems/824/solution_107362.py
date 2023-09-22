#QUESTAO2
def uppCons(frase):
    '''
    A função retorna todas as consoantes
    em maiusculo.
    list -> string
    '''
    i=0
    consoantes = (b,c,d,f,g,j,k,l,m,n,p,q,r,s,t,v,w,x,z)
    while i<len(frase[0]):
        if frase[0] in consoantes:
            frase = frase.upper()
        i = i +1
    return frase