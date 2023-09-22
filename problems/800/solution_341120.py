def total(lCompras,produtos):
    '''Retorna o total da compra a paritr dos
       itens armanezados na lista de entrada e do
       dicionário com o valor de cada produto no
       referido supermercado;
       list, dict -> float'''
    valorTotal=0
    for item in lCompras:
        valorTotal+=produtos[item]
    return round(valorTotal,2)