def total(listacompra,precos):
    ''' Função que retornar o valor total 
    	da compra dos produtos que você colocou na lista.
        list,adic--->float'''
    total=0
    for i in precos:
        if i in listacompra:
            total+=precos[i]
    return round(total,2)