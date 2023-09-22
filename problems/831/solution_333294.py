def lingua_p(palavra):
    """Retorna a palavra recebida na língua do P.
    str->str"""
    minus=palavra.lower()
    NPal= ""
    vogais= "aeiouãáéíóú"
    for pal in minus:
        NPal+=pal
        if pal in vogais:
            NPal+= "p"+pal
    return NPal