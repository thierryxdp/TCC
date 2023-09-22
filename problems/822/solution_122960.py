def repetidos(lista):
    aux = 0
    for i in range(len(lista)):
        if i != 0 :
          	if lista[i+1] == lista[i]:
              	aux += 1

    return aux