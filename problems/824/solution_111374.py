def uppCons(frase):
    leitura=len(frase)
    while i<leitura:
        frasei=frase[i]
        if frasei=!('a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U'):
            k=str.upper(frasei)
            menor=i-1
            frase=frase[0:menor]+k+[i:]
        i=i+1
    return frase