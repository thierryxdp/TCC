def total(compras,produtos):
    for i in produtos:
        if compras in produtos:
            return sum(produtos.values())