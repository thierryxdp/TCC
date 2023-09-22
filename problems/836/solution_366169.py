def busca(setor,funcionarios):
    '''Retorna todos funcionários e suas informações do setor informado
    string,matrix->matrix'''
    res_busca=[]
    for func in funcionarios:
        if func[2]==setor:
            list.append(res_busca,[func[0],func[1],func[3]])
    return res_busca