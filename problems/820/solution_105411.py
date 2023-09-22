def posLetra (texto, letra, ocorrencia):
    """ retorna em qual posição do texto está a ocorrencia da letra.
    string, string, int -> int"""
    if ocorrencia < str.count(texto, letra):
        return -1
    i = 0
    while ocorrencia > 0:
        i = texto.find (letra,i)
        ocorrencia -=1
    return i