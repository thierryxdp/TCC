def busca(setor,M):
    '''
    funcao que recebe uma string e uma matriz M com as informacoes
    dos funcionarios, faz uma busca pelo setor nessa matriz e retorna
    uma nova lista somente com os dados dos funcionarios desse setor
    str,list->list
    '''
    lista=[]
    for m in range(0,len(M)):
        for n in range(0,len(M[m])):
            if setor.lower()==M[m][n].lower():
                dados=M[m].copy()
                dados.pop(dados.index(dados[n]))
                lista.append(dados)
    return lista