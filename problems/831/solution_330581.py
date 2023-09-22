def lingua_p(x):
    "Retorn qualquer frase na lingua do p!; str->str"
    frase=x.lower()
    texto=''
    for i in frase:
        if i in "aeiouáéíóú":
            texto+=i+'p'+i
            
        if i not in "aeiouáéíóú":
            texto+=i
    return texto