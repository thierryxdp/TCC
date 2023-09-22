def busca(setor,M):
    ''' Função que busque no setor informado os dados dos funcionários
str, list -> list'''
    funcionarios_setor = []
    for i in range(len(M)):
        if M[i][2] == setor:
            funcionarios_setor.append(M[i])
    for j in range(len(funcionarios_setor)):
	    funcionarios_setor[j].remove(setor)
    return funcionarios_setor