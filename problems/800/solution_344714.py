# função verificar produtos e retornar valor total a ser pago
def total(lista_compras = [],produtos = {}):
    cont = 0
    for i in lista_compras:
        cont += produtos[i]
        return round(produtos,2)

# Escolha nomes elucidativos para suas variáveis