def lingua_p(palavra):
    '''explicação'''

    palavra = str.lower(palavra)
    
    resultado = ''

    vogais = {'a':'apa',
              'e':'epe',
              'i':'ipi',
              'o':'opo',
              'u':'upu',
              'á':'ápá',
              'é':'épé',
              'í':'ípí',
              'ó':'ópó',
              'ú':'úpú'}

    for i in range(0,len(palavra)):
        resultado = resultado + dict.get(vogais,palavra[i],palavra[i])

    return resultado