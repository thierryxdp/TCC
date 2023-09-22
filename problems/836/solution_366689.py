def busca(setor,lista_funcionarios):
    resultado=[]
    for i in range(0,len(lista_funcionarios)):
        if setor in lista_funcionarios[i]:
            list.append(resultado,lista_funcionarios[i])
            list.remove(resultado,setor)
        else:
            return resultado
    return resultado