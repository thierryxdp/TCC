# 
#
#
#
def total(lista,dicionario):
    i=0
    valor_total=0
    while i<len(lista):
        if lista[i] in dicionario:
            v=dict.get(dicionario,lista[i])
            valor_total=valor_total+v
        i=i+1
    return round(valor_total,2)