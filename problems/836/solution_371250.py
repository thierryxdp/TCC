def busca(setor:str,matriz:list)-> list:
    '''Faz uma buscar por setor de todos os funcionários da empresa'''
    
    def verifica(funcionarios:list)-> bool:
        '''Verifica se os funcionários são de determinado setor ou não'''
        return True if setor in funcionarios else False
    funcionarios_setor1= list(filter(verifica,matriz))
   
	def remove_setor(funcionarios):
        '''Remove o setor no qual o funcionário pertence,
        para retornar apenas o restante dos dados deste'''
        if setor in funcionarios:
            del(funcionarios[2])
    funcionarios_do_setor = list(map(remove_setor, funcionarios))
    return funcionarios_do_setor