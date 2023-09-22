def uppCons(frase):
    lista=[]
    leitura=len(frase)
    while i<leitura:
        frasei=frase[i]
        if frasei!=('a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U'):
            k=str.upper(frasei)
            u=list.append(lista,k)
        i=i+1
    return lista