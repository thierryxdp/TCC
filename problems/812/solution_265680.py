"""
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

"""
Acima temos a função anterior que vai ser usada

Essa função nova recebe uma frase e depois inverte a ordem das palavras e para isso retira qualquer pontuação usando a função "retira_pontuacao"

Assinatura: str --> str
"""

def inverte(frase):

  """
  A função recebe a frase e antes de inverter, essa frase é passada na outra função para retirar as pontuações

  Em seguida a função é fatiada usando "split" e depois invertida a ordem da lista

  Por fim, essa lista invertida é concatenada e retorna a frase invertida
  """

  frase = retira_pontuacao(frase)

  frase = frase.split(" ") [::-1]

  nova_string = ""

  for i in range(len(frase)):

    nova_string = nova_string + " " + frase[i]

  return nova_string