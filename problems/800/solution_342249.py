def total(lis,di):
    i = 0
    soma = 0
    while i < len(lis):
      soma = soma + dict.get(di,lis[i])
      i = i + 1
    return round(soma, 2)