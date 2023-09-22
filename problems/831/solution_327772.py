def lingua_p(palavra):
    '''dada uma palavra, a retorna traduzida para a língua do p,
    inserindo, após cada vogal, a sequência de letras 'p' mais a vogal original;
    str --> str'''
    traduzida = ''
    for letra in str.lower(palavra):
        if letra not in 'qwrtypsdfghjklçzxcvbnm':
            traduzida = traduzida + letra + 'p' + letra
        else:
            traduzida = traduzida + letra
    return traduzida