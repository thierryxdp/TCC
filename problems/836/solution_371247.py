def busca(setor:str,matriz:list)-> list:
    '''Faz uma buscar por setor de todos os funcionários da empresa'''
    def verifica(funcionarios:list)-> bool:
        '''Verifica se os funcionários são de determinado setor ou não'''
        return True if setor in funcionarios else False
    funcionarios_setor= list(filter(verifica,lista))
    def exclui(funcionarios):
        '''Remove o setor no qual o funcionário pertence,
        para retornar apenas o restante dos dados deste'''
        if setor in funcionarios:
            del(fun[2])
    func2 = list(map(exclui, funcionarios))
    return func