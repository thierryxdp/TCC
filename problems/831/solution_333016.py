def lingua_p(palavra):
  '''Função que recebe uma palavra (em português) e retorna esta mesma palavra traduzida para a língua do P'''
  
  palavra_P = ""
  
  for i in palavra.lower():
    if i in "aeiouáéíóú":
      palavra_P += i + 'p' + i
    else:
      palavra_P += i
  
  return palavra_P