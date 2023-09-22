def troca_pontuacao_por_espaco(string):
  """essa função substitui as pontuações da frase dada como parametro por espaços
str->str"""
  string = string.replace('!', ' ')
  string = string.replace('?', ' ')
  string = string.replace('...', ' ')
  string = string.replace('.', ' ')
  string = string.replace('—', ' ')
  string = string.replace(',', ' ')
  string = string.replace(':', ' ')
  string = string.replace(';', ' ')
  return string.replace('  ', ' ')