def busca(nome, contato):
    '''Função que retorna a lista o "nome"de contato está inserido de entrada: lists -> list'''
    
    indice = 0
    solucao = []

    while indice < len(contato):
        if str.lower(nome) in str.lower(contato):
            solucao[len(solucao):len(solucao)] = [contato[indice]]

        indice += 1

    return solucao