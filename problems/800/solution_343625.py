def total(produtos,valores):
    produtos = []
    valors = {}
    totaL = 0
    for produtos in valores:
        if produtos in valores:
            totaL = totaL +valores[produtos]
    return totaL