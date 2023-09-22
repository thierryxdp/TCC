def posLetra(texto,letra,ocor):
    """Retorna em qual posição da string "texto" está aquela
    ocorrência da letra;
    string, string, int -> int"""
    i=1  #contador
    c=-1  #acumulador
    if i == ocor:
        return str.find(texto,letra)
    while i < ocor:
        pos = str.find(texto,letra,c+1)
        c += pos
        i += 1
    return pos