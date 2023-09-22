def inverte(string):
  """dada uma frase como parametro, retorna outra frase invertida sem letras maiusculas e sem pontuacao
str->str"""
  string = troca_pontuacao_por_espaco(string)
  lista_palavras = string.split(' ')
  lista_reversa = lista_palavras[-2::-1]
  return ' '.join(lista_reversa)