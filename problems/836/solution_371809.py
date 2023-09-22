def busca(setor,matriz):
    '''Dado uma matriz e o setor da empresa, retorna os dados de todos
;os funcionários referente ao setor dado pela função.
strig,matriz-->matriz com formato de strig'''
    ocorrencia=[]
    if setor in matriz[0]:
        ocorrencia=ocorrencia+[matriz[0]]
        ocorrencia[0].remove(setor)
        ocorrencia=ocorrencia
    if setor in matriz[1]:
        ocorrencia=ocorrencia+[matriz[1]]
        ocorrencia[0].remove(setor)
    if setor in matriz[2]:
        ocorrencia=ocorrencia+[matriz[2]]
        ocorrencia[1].remove(setor)
    return ocorrencia