def busca(setor,matriz):
    '''Busca informações de contato no setor desejado.
    String, List -> List.'''
    dados = []
    vazio = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
           dados.append(matriz[i])
    for j in range(len(dados)):
        if dados[j][2] == setor:
           del dados[j][2]
    if dados ==  vazio1:
        print('Nenhum Registro encontrado')
    return dados