def eh_quadrada(m):
    ''' Função que determina se uma dada matriz m é quadrada ou não
    list -> bool '''
    if m == []:
        return "True"
    elif range(m) == range(m[0]):
        return "True"
    else:
        return "False"