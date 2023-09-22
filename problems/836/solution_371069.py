def busca(setor,dados):
    '''Função que retorna o cantato dos funcionários de setor em comum de entrada: str, list -> list'''
    contato=[]
    for indice in range(len(dados)):
        if indice2 == (dados[indice][2]):
            contato.append(dados[indice][:2]+[dados[indice][-1]])
    return contato