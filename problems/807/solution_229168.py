def conta_frases(texto):
    """A função retorna a quantidade de frases dentro de uma string denominada "texto" ."""
    cont = 1
    lista = texto.split('.'and'!')
    for c in lista:
        cont +=1
    return cont