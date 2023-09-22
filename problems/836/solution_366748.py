def busca(setor,lista_funcionarios):
    pessoas=[]
    for i in range(len(lista_funcionarios)):
        for j in range(len(lista_funcionarios[i])):
            if setor == lista_funcionarios[i][j]:
                list.append(pessoas,lista_funcionarios[i])
                for k in range(len(pessoas)):
                    if setor == pessoas[j][k]:
                        list.remove(pessoas[k],setor)
    return pessoas