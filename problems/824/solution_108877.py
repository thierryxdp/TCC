def uppCons(frase):
    frase_upp=''
    l=0
    for letra in frase:
        if frase[l]=='a' or frase[l]=='e' or frase[l]=='i' or frase[l]=='o' or frase[l]=='u' or frase[l]=='A' or frase[l]=='E' or frase[l]=='I' or frase[l]=='U' or frase[l]=='Á' or frase[l] =='á' or frase[l] =='É' or frase[l]=='é' or frase[l]=='ó' or frase[l] =='Ó' or frase[l]=='ô' or frase[l]=='Ô' or frase[l]=='ú' or frase[l]=='Ú' or frase[l]==' ':
            frase[l]=frase[l]
        else:
            frase[l]=str.upper(frase[l])
        l=l+1
        frase_upp=frase_upp+frase[l]
    return frase_upp