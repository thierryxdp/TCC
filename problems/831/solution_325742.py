def lingua_p(palavra):
    ''' '''
    traduz = ''
    for letra in(palavra):
        if letra in['aeiouAEIOU']and letra not in['bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ']:
            traduz = traduz + palavra
            traduz = letra + 'p' + letra
            return str.lower(traduz)