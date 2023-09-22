def busca(setor,funcionarios):
    '''Retorna todos funcionários e suas informações do setor informado
    string,matrix->matrix'''
    res_busca=[]
    for func in funcionarios:
        if func[2]==setor:
            list.append(res_busca,func)
    return res_busca