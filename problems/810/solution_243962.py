def inverte(frase):
    """Retorna a frase de entrada invertida; str->str"""
    a1 = str.replace(frase, '.', ' ')
    a2 = str.replace(a1, '!', ' ')
    a3 = str.replace(a2, '?',' ')
    a4 = str.replace(a3, '...',' ')
    a5 = str.replace(a4, '-', ' ')
    a6 = str.replace(a5, ',', ' ')
    a7 = str.replace(a6, ':', ' ')
    a8 = str.replace(a7, ';', ' ')
    diminuir = str.lower(a8)
    separar = str.split(diminuir)
    reverter = list.reverse(separar)
    juntar = str.join(' ', reverter)
    frase = juntar
    return frase