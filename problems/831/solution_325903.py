def lingua_p(palavra):
    '''Dado uma palavra, após cada vogal da palavra original,
    é inserida a sequência de letras 'p' mais a vogal original.
    str --> str'''
    str.lower(palavra)
    a = list(palavra)
    b = ''
    prox = 0
    while prox < len(a):
        if 'a' == a[prox]:
            b = b + a[prox] + 'pa'
            
        elif 'e' == a [prox]:
            b = b + a[prox] + 'pe'
            
        elif 'i' == a[prox]:
            b = b + a[prox] + 'pi'

        elif 'o' == a[prox]:
            b = b + a[prox] + 'po'

        elif 'u' == a[prox]:
            b = b + a[prox] + 'pu'

        else:
            b = b+ a[prox]

        prox = prox + 1
    return b