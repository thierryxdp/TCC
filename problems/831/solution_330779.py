def lingua_p(palavra):
    '''explicação'''

    palavra = str.lower(palavra)
    
    resultado = ''

    vogais = {'a':'apa',
              'e':'epe',
              'i':'ipi',
              'o':'opo',
              'u':'upu',
              'á':'apa',
              'é':'epe',
              'í':'ipi',
              'ó':'opo',
              'ú':'upu'}

    for i in range(0,len(palavra)):
        resultado = resultado + dict.get(vogais,palavra[i],palavra[i])

    return resultado