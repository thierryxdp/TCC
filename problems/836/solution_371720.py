def busca(setor,matriz):
    '''dada uma matriz com nome de funcionario, registro,
    setor e numero de telefone; essa funçao nos retorna 
    uma lista dos funcionarios que trabalham no setor 
    inserido na entrada da funçao e retornam seus registros 
    e numeros de telefone
    str.,lista-->lista'''
    y=[]
    for i in range(len(matriz)):
                   if setor in matriz[i]:
                		matriz[i].remove(setor)
                	    y=y+[matriz[i]]
    return y