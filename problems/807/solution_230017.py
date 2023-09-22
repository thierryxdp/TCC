def conta_frases(string):
  """Essa função conta quantas frases aparecem em um texto
str->int"""
  string = string.replace('!', '!!')
  string = string.replace('?', '!!')
  string = string.replace('...', '!!')
  string = string.replace('.', '!!')
  return len(string.split('!!')) - 1