def busca(setor,matriz):
    '''busca um funcionario no setor
    str'''
    func=[]
    for i in matriz:
            if setor in i:
                func+=[[i[0],i[1],i[3]]]
            if len(func)==0:
                return 'Nenhum funcionário'
    return func