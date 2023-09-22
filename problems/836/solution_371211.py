def busca(funcao,lista):
    func=map(lambda x: [lista[x][0]+lista[x][1]+lista[x][3]] if funcao[x] in lista[x]else [],range(len(lista)))
    return list(func)