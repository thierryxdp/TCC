def retira_pontuacao(texto):
    '''retira toda a pontuacao de uma frase dada, incluindo,vírgula,dois pontos,travessao
      str->str'''
    texto = texto.replace(('-'), ' ')
    texto = texto.replace((','), ' ')
    texto = texto.replace((':'), ' ')
    texto = texto.replace((';'), ' ')
    texto = texto.replace(('.'), ' ')
    texto = texto.replace(('!'), ' ')
    texto = texto.replace(('?'), ' ')
    return texto