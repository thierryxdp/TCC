def melhor_volta(m):
    contagem = 0
    lista = []
    total = 0
    for i in m:
        lista.append(i.min())
    primeiro = lista.min()
    return primeiro