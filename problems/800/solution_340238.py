def total(listacomp,precos):
    'recebe uma lista de compras e um dicionario com o preço dos produtos e calula o valor final da compra, list,dict-->float'
    valor=0
    for i in listacomp:
        valor+=precos[i]
    return valor