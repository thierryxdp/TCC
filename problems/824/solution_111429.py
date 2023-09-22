def uppCons(frase):
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