def lingua_p(palavra):
    '''Dada uma palavra, a função retorna a mesma traduzida para a 
       língua do p
       str -> str
       Parametros:
       palavra: palavra a ser digitada'''
    palavrap = []
    palavra = str.lower(palavra)
    palavra = list(palavra)
    for c in range(0, len(palavra)):
        if palavra[c] in 'aeiouãõáéíóú':
            palavrap.append(palavra[c])
            palavrap.append('p')
            palavrap.append(palavra[c])
        else:
            palavrap.append(palavra[c])
    return palavrap.join('')