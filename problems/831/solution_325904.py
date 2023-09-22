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
            
        elif 'ã' == a[prox]:
            b = b + a[prox] + 'pã'
            
        elif 'á' == a [prox]:
            b = b + a[prox] + 'pá'
            
        elif 'â' == a[prox]:
            b = b + a[prox] + 'pâ'
            
        elif 'e' == a [prox]:
            b = b + a[prox] + 'pe'
            
        elif 'é' == a [prox]:
            b = b + a[prox] + 'pé'
            
        elif 'ê' == a[prox]:
            b = b + a[prox] + 'pê'
            
        elif 'i' == a[prox]:
            b = b + a[prox] + 'pi'
        
        elif 'í' == a[prox]:
            b = b + a[prox] + 'pí'

        elif 'o' == a[prox]:
            b = b + a[prox] + 'po'
            
        elif 'ó' == a[prox]:
            b = b + a[prox] + 'pó'
            
        elif 'ô' == a[prox]:
            b = b + a[prox] + 'pô'
            
        elif 'õ' == a[prox]:
            b = b + a[prox] + 'põ'

        elif 'u' == a[prox]:
            b = b + a[prox] + 'pu'
            
        elif 'ú' == a[prox]:
            b = b + a[prox] + 'pú'

        else:
            b = b+ a[prox]

        prox = prox + 1
    return b