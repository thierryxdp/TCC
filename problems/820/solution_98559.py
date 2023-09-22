def posLetra(texto,letra,ocor):
    """Retorna em qual posição da string "texto" está aquela
    ocorrência da letra;
    string, string, int -> int"""
    i=0  #contador
    c=-1  #acumulador
    if ocor ==1:
        return str.find(texto,letra)
    while i < ocor:
        pos = str.find(texto,letra,c+1)
        c += pos+1
        i += 1
    return pos