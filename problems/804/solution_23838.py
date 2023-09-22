def filtra_pares(tupla):
    """Monta uma nova tupla apenas com os pares da fornecida
    assinatura: int, int, int, int --> int
    """
    tuplapares=()
    if tupla[0]%2==0:
        tupla = tupla + (tupla[0], )                            
    if tupla[1]%2==0:
        tupla = tupla + (tupla[1], )
    if tupla[2]%2==0:
        tupla = tupla + (tupla[2],)
    return tuplapares