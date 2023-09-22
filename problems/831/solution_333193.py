#Função que recebe uma palavras(em português) e traduz ela para linguagem do P
def lingua_p(palavra):   
    indice = 0
    traducao = list(palavra)
    trad = ''
   
    while indice < len(palavra):
          trad = trad + traducao[indice]
          if palavra[indice] in 'aeiouAEIOUãé':
             trad = trad + 'p' + traducao[indice]
          indice = indice + 1
    return str.lower(trad)