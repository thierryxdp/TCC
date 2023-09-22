def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna a mesma palavra
    traduzida para a língua do P; string -> string'''
    
    indice = 0
    traducao = list(palavra)
    trad = ''
    while indice < len(palavra):
          trad = trad + traducao[indice]
          if palavra[indice] in 'aeiouAEIOUãé':
             trad = trad + 'p' + traducao[indice]
          indice = indice + 1
    return str.lower(trad)