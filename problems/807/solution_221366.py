def conta_frases(texto):
    partes_texto1=(str.split(texto, '.'))
    n1=len(partes_texto1)
    partes_texto2=(str.split(texto, '?'))
    n2=len(partes_texto2)
    partes_texto3=(str.split(texto, '!'))
    n3=len(partes_texto3)
    partes_texto4=(str.split(texto, '...'))
    n4=len(partes_texto3)
    
    return n1+n2+n3+n4+n5