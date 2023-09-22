def lingua_p(frase):
    frase=str.lower(frase)
    texto=''
    for i in frase:
        if i in "aeiouáéíóú":
            texto+=i+'p'+i
            
        if i not in "aeiouáéíóú":
            texto+=i
    return texto