def busca(setor,lista):
    """dado uma lista com lista de contatos de funcionarios e o numero de um setor, retorna as informações desse setor; str, list -> list"""
    a=[]
    for x in lista:
        for y in x:
            for z in y:
                if setor==z:
                    list.append(a,x)
    return a
    else:
        return []