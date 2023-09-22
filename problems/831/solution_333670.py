vogais = ['a','e','i','o','u','á','é','í','ó','ú']
def lingua_p(palavra):
    palavrap = ''
    i = 1
    while i < len(palavra):
        palavrap += palavra[i]
                i += 1
        for vogal in vogais:
            if palavra[i] == vogal:
                palavrap += 'p' + vogal
    return palavrap