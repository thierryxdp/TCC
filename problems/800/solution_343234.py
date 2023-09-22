def total(listaDeCompras,dicionario):
    x=0.000
    for i in dicionario:
        if i==listaDeCompras:
            x=x+round((x+dicionario[i]),2)
        return x