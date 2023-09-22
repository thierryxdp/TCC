def eh_quadrada(sq):
    rows = len(sq)
    for row in sq:
        if len(row) != rows:
            return False
    return True