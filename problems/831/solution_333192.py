def lingua_p(palavra):
    '''.'''
    i = 0
    vogal = 'aeiouAEIOU'
    for vogal in palavra:
        palavra = 'p' + palavra[i:]
        i = i + 1
    return palavra