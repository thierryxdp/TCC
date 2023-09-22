def repetidos(lista_num):
    """ retorna o numero e vezes que um
    elemento da lista e igual ao anterior.
    list -> int"""
    i = 0
    repeticoes = 0
    while i < len(lista_num):
      if lista_num[i] == lista_num[i-1]:
        repeticoes += 1
      i += 1
    return repeticoes