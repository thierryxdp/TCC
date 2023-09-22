def busca(Procurar, Matriz):
    lista = []
    lista2 = []
    for linha in Matriz:
        if Procurar in linha:
        	lista += [linha]
            for linha2 in lista:
                print(linha2)