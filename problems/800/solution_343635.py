#2
'''
retorna soma de itens do dict
list, dict -> float
'''
def total(itemsList, totalDict):
  total = 0

  for value in totalDict:
    if value in itemsList:
      total = total + float(totalDict[value])
  return total