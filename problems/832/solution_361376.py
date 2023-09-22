def eh_quadrada(m):
    '''Funçao calcula e retorna se a matriz é quadrada(true) ou não(false). list(list)->bool'''
    if m == []:
        return True
    l = len(m)
    c = len(m[0])
    if l == c:
        return True
    else:
        return False