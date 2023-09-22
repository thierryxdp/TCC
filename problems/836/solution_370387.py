def busca(setor,lista):
    """"função dado o nome de um setor da empresa, retorna uma lista com os 
    dados de todos os funcionários daquele setor;
    str,list->list"""
    lr=[]
    for i in lista:
        if setor in i:
            list.append(lr,[i[0],i[1],i[3]])
    return lr