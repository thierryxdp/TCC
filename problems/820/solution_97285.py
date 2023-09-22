def posLetra(frase,letra,numero):
    """Função que retorna em que posição a ocorrência estava
        str,str,int->int"""
    i = 0
    ocor = 0
    a = str.count(frase,letra)
    
    if a < numero:
        return -1
    
    while ocor < numero:
        if frase[i] == letra:
             ocor += 1
        i += 1
    return i-1