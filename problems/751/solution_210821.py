"""
A função recebe uma string representando uma frase e retorna o número de palavras

Assinatura: str --> int
"""

def quant_palavras(frase):

  """
  Como queremos considerar que a frase possa ter um espaço no começo e no final da frase eu fiz o seguinte: separei a frase com "split" mas caso a frase tenha espaço no começo ou no final, esse espaço é levado em consideração quando a string é fatiada. Para contornar isso eu usei um loop for que verifica cada posição da lista "separador". Caso a posição daquela lista seja diferente de vazia então é adicionada +1 ao contador "palavras". No final da verificação é retornado esse contador que significa o número de palavras na frase
  """

  separador = frase.split(" ")

  palavras = 0

  for i in range(len(separador)):

    if separador[i] != "":

      palavras = palavras + 1

  return palavras