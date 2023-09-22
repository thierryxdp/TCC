def busca(setor,M):
    ''' Função que busque no setor informado os dados dos funcionários
str, list -> list'''
    funcionarios_setor = []
    for i in range(len(M)):
        if M[i][2] == setor:
            funcionarios_setor.append(M[i])
            funcionarios_setor.remove(str(M[i][2]))
            
    return funcionarios_setor