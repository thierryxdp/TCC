def busca(setor,lista_funcionarios):
    pessoas=[]
    k=0
    for i in range(len(lista_funcionarios)):
        for j in range(len(lista_funcionarios[i])):
            if setor == lista_funcionarios[i][j]:
                list.append(pessoas,lista_funcionarios[i])
                while k<len(pessoas):
                    if setor in pessoas[k]:
                        k=k+1
                        list.remove(pessoas[k],setor)
    return pessoas