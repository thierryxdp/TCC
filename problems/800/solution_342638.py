def total(lista,produto):
     '''Funcao que recebe uma lista com 3 intens e um
     dicionario com os preços e retorna o valor total
     dos intens dessa lista de acordo com os preços
     contidos no dicionario.
     list, dict --> float
    '''
     i = 0
     valor_total = 0

     for elementos in lista:
        if lista[i] in produto:
            valor_total += produto[lista[i]]
     return round(valor_total,2)