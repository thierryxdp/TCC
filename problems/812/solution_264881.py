def retira_pontuacao(frase):
    '''retorna uma frase sem pontos e preenchida com espaços
      str -> str'''
    l1= str.replace(frase, ('?'), ' ' )
    l2 = str.replace(frase, ('!'), ' ' )
    l3 = str.replace(frase, (','), ' ' )
    l4 = str.replace(frase, ('-'), ' ' )
    pontos = l1,l2,l3,l4
    return pontos