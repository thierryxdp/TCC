def filtra_pares(tupla):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    if tupla[0]%2==0:
        tupla1 = (tupla[0],)
    if tupla[1]%2==0:
        tupla2 = tupla1 + (tupla[1],)
    if tupla[2]%2==0:
        tupla3 = tupla2 + (tupla[2],)
    if tupla[3]%2==0:
        tupla4 = tupla3 + (tupla[3],)
    return tupla4