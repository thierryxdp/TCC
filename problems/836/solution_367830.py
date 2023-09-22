def busca(setor,matriz):
    '''busca um funcionario no setor
    str,list(list)->list(list)'''
    func=[]
    for i in matriz:
            if setor in i:
                func+=[[i[0],i[1],i[3]]]
        if len(func)==0:
       Return '''Nenhum funcionário encontrado'''
	 Else:
      Return func