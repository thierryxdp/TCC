def lingua_p(palavra):
    minus=palavra.lower()
    NPal= ""
    vogais= "aeiouãáéíóú"
    for pal in minus:
        NPal+=pal
        if pal in vogais:
            NPal+= "pal"+pal
    return NPal