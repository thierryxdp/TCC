"""
Essa função recebe uma frase e retorna outra frase só que com as consoantes maiúsculas

Assinatura: str --> str
"""

def uppCons(frase):

  """
  Primeiro eu declarei uma varíavel que é a frase passada em formato de lista  e outra que é uma string vazia

  Depois disso é usado um for e um if para verificar se a letra é uma consoante e caso seja foi usado a função upper do Python que transforma a string em maiúscula 

  Por fim, usando a lista foi reescrita e retornada
  """

  frase_lista = list(frase)
  frase_final = ""

  for i in range(len(frase_lista)):

    if frase_lista[i] in ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","ç","Ç","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]:

      frase_lista[i] = frase_lista[i].upper()

  for i in range(len(frase_lista)):

    frase_final = frase_final + frase_lista[i]

  return frase_final