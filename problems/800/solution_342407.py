def total(lista,dic):
    soma = 0
    for e in lista:
      e=dic[e]
      soma=soma+e
    return soma