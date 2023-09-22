def lingua_p(palavra):
    frase=''
    vogas='aeiouAEIOUéíú'
    vogais.lower()
    for i in palavra:
        if i in vogais:
            frase=frase+i+'p'+i
        else:
            frase=frase+i
            
    return frase