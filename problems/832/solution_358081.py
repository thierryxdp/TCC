def eh_quadrada(m:list):
    linhas = len(m)
    if len(m) == 0:
        return True
    if linhas == len(m[0]):
        return True
    if linhas != len(m[0]):
        return False