#A funcao recebe uma lista de compras e um dicionario contendo o preco de cada
#produto disponivel em uma determinada loja e retorna o valor total dos itens
#da lista que estejam disponiveis nesta loja.
#lis eh a lista recebida e di eh o dicionario recebido.
#list, dict > float

def total(lis,di):
    i = 0
    soma = 0
    while i < len(lis):
      soma = soma + dict.get(di,lis[i])
      i = i + 1
    return round(soma, 2)