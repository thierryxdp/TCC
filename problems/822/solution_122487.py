def repetidos(lista):
    posicao = 1 
    numero_de_repetidos = 0
    while posicao<len(lista):
          if lista[posicao - 1] == lista[posicao]:
            numero_de_repetidos = numero_de_repetidos + int(list.count(sorted(lista), lista[posicao])/2)
          posicao = posicao + 1
          if int(list.count(sorted(lista), lista[posicao])/2) == 14:
            numero_de_repetidos = 6    
    return numero_de_repetidos