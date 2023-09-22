vogais = ['a','e','i','o','u']
def lingua_p(palavra):
    palavrap = ''
    for i in range(len(palavra)):
        palavrap += palavrap[i]
        for vogal in vogais:
            if palavra[i] == vogal:
                palavrap += 'p' + vogal
    return palavrap