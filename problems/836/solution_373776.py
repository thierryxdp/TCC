def busca(setor,matriz):
    '''Dados uma matriz e um valor procurado (setor), retorna as informações
    de cada linha da matriz que contenham o valor procurado
    str, list(list,list,...) --> list(list,list,...)'''
    
    lista_de_dados = []
    for linha in matriz:
        if setor in linha:
            dados = []
            for info in linha:
                if info != setor:
                    dados.append(info)
            lista_de_dados.append(dados)
    return lista_de_dados