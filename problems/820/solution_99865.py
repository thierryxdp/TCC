def posLetra(texto,busca,n):
    """retorna a ocorrencia da letra
    str,str,str->str"""
    pos= texto.find(busca)
    while pos>= 0 and n > 1:
        pos = texto.find(busca,pos + 1)
        n-= 1
    return pos