# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,preco):
    '''A funcao recebe uma lista de compras e o preco dos produtos de um mercado e
retorna o valor total da compra dos itens da lista list,dic->int'''
    precos=[]
    for i in lista:
        if i in dict.keys(preco):
            precos.append(preco[i])
    return round(sum(precos),2)