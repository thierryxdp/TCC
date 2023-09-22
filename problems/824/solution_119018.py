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

    if frase_lista[i] != "a" and frase_lista[i] != "e" and frase_lista[i] != "i" and frase_lista[i] != "o" and frase_lista[i] != "u":

      frase_lista[i] = frase_lista[i].upper()

  for i in range(len(frase_lista)):

    frase_final = frase_final + frase_lista[i]

  return frase_final