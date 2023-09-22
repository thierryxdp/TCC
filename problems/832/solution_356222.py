def eh_quadrada (a):
    'função classifica a matriz dada como True, caso ela seja quadrada ou vazia, ou False, caso não seja. str -> str'
    if a == []:
        return True
    elif len(a) == len(a[0]):
        return True
    else:
        return False