def busca(setor,M):
    ''' Função que busque no setor informado os dados dos funcionários
str, list -> list'''
    funcionarios_setor = []
    apagar = ''
    for i in range(len(M)):
        if M[i][2] == setor:
            funcionarios_setor.append(M[i])
    funcionarios_setor = funcionarios_setor[0]
    apagar = funcionarios_setor[2]
    funcionarios_setor.remove(apagar)
    return [funcionarios_setor]