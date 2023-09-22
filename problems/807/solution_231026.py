"""
A função é semelhante a última só que no lugar de palavras por frases é frases por texto. O texto é recebido como parâmetro na função que retorna a quantidade de frases nesse texto

Assinatura: str --> int
"""

def conta_frases(texto):

  """
  Como estamos lidando com um texto, podemos nos deparar com diversos pontos como por exemplos ".", "?", "!", entre outros.

  Dessa forma, tive que fazer um split para cada um dos casos e para isso, a cada split, eu juntei a frase novamente para dar outro split e no final passei um "for" para verificar algum indíce vazio na lista "separador"
  """

  separador = texto.split(".")

  nova_string = ""

  for i in range(len(separador)):

    nova_string = nova_string + separador[i] + "-"
  
  separador = nova_string.sp…
[13:55, 28/05/2022] Alexandre Ufrj: """
Essa função recebe uma frase e retorna a frase sem as pontuações da língua portuguesa e no lugar das pontuações é retornada um "espaço"

Assinatura: str --> str
"""

def retira_pontuacao(frase):

  """
  O funcionamento dessa função é simples: usando a função do Python "replace" foi trabalhada com um dos casos de pontuação e essa função foi usada para cada um dos casos e por fim, a frase foi retornada
  """

  frase = frase.replace("-"," ")
  frase = frase.replace(":"," ")
  frase = frase.replace(","," ")
  frase = frase.replace(";"," ")
  frase = frase.replace("..."," ")
  frase = frase.replace("!"," ")
  frase = frase.replace("?"," ")
  frase = frase.replace("."," ")

  return frase