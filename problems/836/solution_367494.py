def busca():
    lin = int(input("N° de linhas: "))
    matriz = []
    for x in range (lin):
        linha = []
        for y in range(4):
            if y == 0:
                info = input("Digite o seu NOME: ")
                linha.append(info)
            elif y == 1:
                info = input("Digite o seu ID: ")
                linha.append(info) 
            elif y == 2:
                info = input("Digite o seu SETOR: ")
                linha.append(info)
            elif y == 3:
                info = input("Digite o seu TELEFONE: ")
                linha.append(info)
        matriz.append(linha)
    buscar = input("Digite o setor que voce deseja pesquisar: ")
    localizar = []
    for x in range(0,len(matriz)):
        if buscar in matriz[x][2]):
            del(matriz[x][2])
            list.append(localizar,matriz[x])
    if len(localizar) == 0:
        return "Nenhum registo encontrado"
    else:
        localizar