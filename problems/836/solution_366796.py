def busca(setor,lista_funcionarios):
    pessoas=[]
    for i in range(len(lista_funcionarios)):
        
        if setor in lista_funcionarios[i]:
                pessoas.append(i[0])
    return pessoas