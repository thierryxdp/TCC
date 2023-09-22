def lingua_p(palavra):
    frase=''
    vogais='aeiouAEIOUéíú'
    palavra.lower()
    for i in palavra:
        if i in vogais:
            frase=frase+i+'p'+i
        else:
            frase=frase+i
            
    return frase