def Consoantes(frase):
    lista=[]
    lista2=['a','e','i','o','u','A','E','I','O','U']
    leitura=len(frase)
    i=0
    while i<leitura:
        frasei=frase[i]
        if ((frasei in lista2)==False):
            k=str.upper(frasei)
            u=list.append(lista,k)
        i=i+1
    return lista
def espaco(frase):
    lista=Consoantes(frase)
    n=len(lista)
    i=0
    while i<n:
        if (' ' in lista)==True:
            list.remove(lista,' ')
        elif ('!' in lista)==True:
            list.remove(lista,'!')
        elif ('?' in lista)==True:
            list.remove(lista,'?')
        elif ('.' in lista)==True:
            list.remove(lista,'.')
        elif (',' in lista)==True:
            list.remove(lista,',')
        i=i+1   
    return lista    
def uppCons(frase):
    lista=espaco(frase)
    l=len(frase)
    i=0
    while i<l:
        if (frase[i] in lista)==True:
            k=i-1
            frase=frase[0:k]+frase[i]+frase[i:]
        i=i+1
    return frase