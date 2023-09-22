def total(listaDeCompras,dicionario):
    x=0.00
    for i in dicionario:
        if i==listaDeCompras:
            x=x+round((x+dicionario[i]),2)
        return x