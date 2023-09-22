# Função para calcular gasto no supermercado
def total (lista,dic):
    #list,dic --> float
    valor=0
    for i in lista:
        #verifica se itens da lista estão no dicionário
        if i in dic:
            valor=valor+dic[i]
    return valor