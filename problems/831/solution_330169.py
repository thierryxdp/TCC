def lingua_p(palavra):
    frase=''
    vogais='aeiouAEIOU'
    for i in palavra:
        if i in vogais:
            frase=frase+i+'p'+i
        else:
            frase=frase+i
            
    return frase