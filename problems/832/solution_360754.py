def eh_quadrada(m):
    "Verifique se a matrix é quadrada; lista(lista)->bool"
    if not m:
        return True
    if len(m)==len(m[0]):
        return True
    else:
        return False