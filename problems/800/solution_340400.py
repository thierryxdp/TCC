def total (lista,precos):
    total=0
    for produtos in lista:
        if produtos in precos:
          valores=precos[produtos]
        total+=valores
    return total
'''dado uma lista de produtos e um dicionário, retorna o 
valor total dos itens presentes na lista
list,dict->float'''