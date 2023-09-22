def busca(setor,lista_funcionarios):
    """Essa função retorna a ficha de uma pessoa dado um setor"""
    """str,list->list"""
    pessoas=[]
    k=0
    for i in range(len(lista_funcionarios)):
        for j in range(len(lista_funcionarios[i])):
            if setor == lista_funcionarios[i][j]:
                list.append(pessoas,lista_funcionarios[i])
    for k in range(len(pessoas)):
         if setor in pessoas[k]:
            list.remove(pessoas[k],setor)
    return pessoas