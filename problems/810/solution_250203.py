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
  string = string.replace('-', ' ')
  return string.replace('  ', ' ')






def inverte(string):
  """dada uma frase como parametro, retorna outra frase invertida sem letras maiusculas e sem pontuacao
str->str"""
  string = troca_pontuacao_por_espaco(string)
  lista_palavras = string.split(' ')
  lista_reversa = lista_palavras[-2::-1]
  lista_minuscula = lista_palavras.lower( )
  return ' '.join(lista_palavras)