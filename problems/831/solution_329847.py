def lingua_p(x):
    frase=x.lower()
    texto=''
    for i in frase:
        if i in "aeiouáéíóú":
            texto+=i+'p'+i
            
        if i not in "aeiouáéíóú":
            texto+=i
    return texto