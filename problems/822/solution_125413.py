def repetidos(lista):
    ''''''
i=0
  while i < len(lista):
        if lista[i] != lista[i+1]:
            repeticoes = lista.count(i)
        i=+1
    return repeticoes