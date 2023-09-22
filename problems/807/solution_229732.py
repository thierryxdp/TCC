def conta_frases(string):
    """
    Essa função dado um texto ira retornar a quantidade
    de frases presentes no mesmo.
    str->int
    """
    if string [-1] == '.' and string[-2] == '.':
        qtdf = str.count(string,'!') + str.count(string,'. ') + str.count(string,'...') +str.count(string,'?')
    elif string [-1] == '.' and string[-2] != '.':
         qtdf = str.count(string,'!') + str.count(string,'. ') + str.count(string,'...') + 1 + str.count(string,'?')
    else:
         qtdf = str.count(string,'!') + str.count(string,'. ') + str.count(string,'...') + str.count(string,'?')
    return qtdf