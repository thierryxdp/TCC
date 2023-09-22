def uppCons(frase):
    lista=[]
    lista2=['a','e','i','o','u','A','E','I','O','U']
    leitura=len(frase)
    i=0
    while i<leitura:
        frasei=frase[i]
        if ((frasei in lista2)==False) and i>0:
            k=str.upper(frasei)
            u=list.append(lista,k)
            menor=i-1
            frase=frase[0:menor]+k+[i:]
        elif ((frasei in lista2)==False) and i==0:
            k=str.upper(frasei)
            u=list.append(lista,k)
            frase[0]=k
        i=i+1
    return lista