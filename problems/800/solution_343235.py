def total(listaDeCompras,dicionario):
    x=round(0,2)
    for i in dicionario:
        if i==listaDeCompras:
            x=x+round((x+dicionario[i]),2)
        return x