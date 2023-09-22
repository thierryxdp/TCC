def posLetra(string, char, number):
  """essa funcao retorna em que posição da string a letra esta dados como parâmetros uma string, a letra e um inteiro que indica a ocorrencia desejada da letra, se tiver menos ocorrencia da letra que a pedida a função retorna -1
    str,int->str"""
  matches_found = 0
  for i in range(len(string) - 1):
    if string[i] == char:
      matches_found += 1

      if matches_found == number:
        return i

  return -1