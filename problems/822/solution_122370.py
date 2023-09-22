def repetidos(lista):
    posicao = 0 
    numero_de_repetidos = 0
    while posicao<len(lista) - 1:
          numero_de_repetidos = numero_de_repetidos + list.count(lista,lista[len(frase) - posicao] == lista[len(frase) - posicao + 1])
          posicao = posicao + 1
    return numero_de_repetidos