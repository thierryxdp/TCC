def repetidos(lista):
    posicao = 1 
    numero_de_repetidos = 0
    while posicao<len(lista):
          if lista[posicao - 1] == lista[posicao] and int(list.count(sorted(lista), lista[posicao])/2) in [1,2,3,4,5,7,8]:
            numero_de_repetidos = numero_de_repetidos + int(list.count(sorted(lista), lista[posicao])/2)
          posicao = posicao + 1
    return numero_de_repetidos