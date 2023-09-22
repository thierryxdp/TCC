def conta_frases(texto):
    """A função retorna a quantidade de frases dentro de uma string denominada "texto" ."""
    cont = 0
    lista = texto.split('.'and'!'and'?'and'...'and';')
    for c in lista:
        cont +=1
    return cont