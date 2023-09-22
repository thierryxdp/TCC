def busca(setor:str,matriz:list)-> list:
    '''Faz uma buscar por setor de todos os funcionários da empresa'''
    
    def verifica(matriz:list)-> bool:
        '''Verifica se os funcionários são de determinado setor ou não'''
        return True if setor in fmatriz else False
    funcionarios_setor = list(filter(verifica,matriz))
   
	def remove_setor(funcionarios1):
        '''Remove o setor no qual o funcionário pertence,
        para retornar apenas o restante dos dados deste'''
        if setor in funcionarios1:
            del(funcionarios1[2])
    funcionarios_do_setor = list(map(remove_setor, funcionarios_setor))
    return funcionarios_do_setor