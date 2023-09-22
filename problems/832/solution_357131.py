def eh_quadrada(M):
    """dada uma matriz, função identifica se ela é quadrada. Se for quadrada,
função retorna True, se não , retorna False. List -> Bool"""
    if len (M) == len(M[0]) or M == [[]]:
        return True
    else:
        return False