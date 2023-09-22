def lingua_p(palavra):
    """ """
    s = ''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            s = s + palavra[i] + 'p' + palavra[i]
        else:
            s = s + palavra[i]