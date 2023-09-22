def uppCons(frase):
    """funcao que recebe uma frase, e retorna-a, mas com seus consoantes em maiusculos;
    str -> str"""
    fraseCons=frase
    i=0
    while i<len(frase):
        if frase[i] not in "aeiouáéíóúãõ":
            fraseCons=str.replace(fraseCons,frase[i],str.upper(frase[i]))
        i=i+1
    return fraseCons