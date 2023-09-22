def busca(setor,mt):
    '''Dado uma matriz e o setor da empresa, retorna os dados de todos
os funcionários referente ao setor dado pela função. strig,matriz-->matriz com formato de strig'''
    ocorrencia=[]
    for i in range(len(mt)):
        if setor in mt[i]:
            mt[i].remove(setor)
            ocorrencia=ocorrencia+[mt[i]]
            return ocorrencia