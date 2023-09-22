def busca(setor,matrizfuncionarios):
    '''Retorna os dados dos funcionários de um certo setor
    entrada: str, list
    saída: list
    '''
    dadosfuncionarios=[]
    for funcionario in matrizfuncionarios:
        if funcionario[2] == setor:
            dadosdofuncionario= [funcionario[0:2]+funcionario[3]]
            dadosfuncionarios=dadosfuncionarios+dadosdofuncionario
    return dadosfuncionarios