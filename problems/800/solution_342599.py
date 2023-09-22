def total(compra):
    productos={'Lentilha': 4.11, 'Massas': 2.39, 'Extrato tomate': 4.84, 'Grão de bico': 7.49, 'Queijo ralado': 9.6, 'Catchup': 7.19, 'Orégano': 1.47, 'Chá': 9.08, 'Farinha rosca': 6.72, 'Vinagre': 8.51, 'Far.mandioca': 8.91, 'Maionese': 7.61, 'Palmito': 8.22, 'Feijão': 6.32, 'Maizena': 8.23, 'Farinha trigo': 4.42, 'Arroz': 1.93, 'Noz-moscada': 1.03, 'Leite condens.': 6.55, 'Azeitonas': 9.51, 'Molho tomate': 8.31, 'Creme leite': 3.34, 'Leite coco': 2.75, 'Gelatina pó': 9.11, 'Chocolate pó': 6.81, 'Açúcar': 9.39, 'Sal': 4.9, 'Louro': 1.68}
    P=list(dict.keys(productos))
    V=list(dict.values(productos))
    r=len(compra)
    z=0
    x=[]
    lista=[]
    while z<r:
        c=P.index(compra[z])
        x.append((V[c]))
        z=z+1
    t=sum(x)
    return (t)