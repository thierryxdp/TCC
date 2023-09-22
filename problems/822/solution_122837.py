def repetidos(qtd):
    lista= [1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]
    contador= counter(lista)
    repetidos=[ item for item,quantidade in contador.items()
               if quantidade>1]
    repetidos= len(repetidos)
    return qtd