def total(listacompras,produtos):
    conta = 0
    for c in listacompras:
        if c in produtos:
            conta += produtos.get(c)
    return round(conta,2)