def filtra_pares(tupla):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    if tupla[0]%2==0:
        tupla = (tupla[0])
    if tupla[1]%2==0:
        tupla = tupla + (tupla[1])
    if tupla[2]%2==0:
        tupla = tupla + (tupla[2])
    if tupla[3]%2==0:
        tupla = tupla + (tupla[3])
    return tupla