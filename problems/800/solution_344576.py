def total(list, dict):
    compras = list
    valores = ()
    for n in dict:
        if n in list:
            valores = valores + (dict.keys())
            return sum(valores)