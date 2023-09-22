# Retorna o valor total dos itens da lista que estejam disponível em uma loja
# list,dic->float 
def total(lista,produtos):
    preco=[]
    for item in lista:
    	preco.append(produtos[item])
    return(sum(preco))