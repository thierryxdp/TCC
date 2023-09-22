def lista_(lista):
    return [lista[0]+lista[1]+lista[3]]
def busca(funcao,lista):
    func=filter(lambda x: 1 if funcao in lista[x]else 0,range(len(lista)))
    lista1=map(lista_,list(func))
    return list(lista1)