def lingua_p(palavra):
    '''função que recebe uma palavra como parametro e retorna esta mesma palavra traduzida para lingua do p; str->str '''
    traduz = ''
    for i in range(len(palavra)):
        if palavra[i] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            traduz = traduz + palavra[i]
             else:
                    traduz = traduz + palavra[i] + 'p' + palavra[i]
                    return traduz