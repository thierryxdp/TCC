# função verificar produtos e retornar valor total a ser pago
def total(lista_compras = [],produtos {}):
    i = 0.0
    for i in lista_compras:
        i += produtos[i]
        return round(i,2)

# Escolha nomes elucidativos para suas variáveis