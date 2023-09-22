def uppCons(frase):
    frase_upp=''
    l=0
    letra=frase[l]
    for letra in frase:
        if frase[l]=='a' or frase[l]=='e' or frase[l]=='i' or frase[l]=='o' or frase[l]=='u' or frase[l]=='A' or frase[l]=='E' or frase[l]=='I' or frase[l]=='U' or frase[l]=='Á' or frase[l] =='á' or frase[l]=='ã' or frase[l]=='Ã' or frase[l] =='É' or frase[l]=='é' or frase[l]=='ó' or frase[l] =='Ó' or frase[l]=='ô' or frase[l]=='Ô' or frase[l]=='ú' or frase[l]=='Ú' or frase[l]==' ':
            letra=letra
        else:
            letra=str.upper(letra)
        l=l+1
        frase_upp=frase_upp+letra
    return frase_upp