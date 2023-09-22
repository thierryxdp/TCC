def busca(setor,matriz):
    ''' função que recebe como entrada o nome de um setor de interesse,
    em string, e uma matriz com 4 colunas contendo informações de 
    funcionários de uma empresa, sendo a primeira coluna referente ao nome
    do funcionário, a segunda ao seu registro, a terceira ao seu setor, e a
    quarta ao seu telefone; o número de linhas é igual ao número de
    funcionários; retorna uma lista das listas contendo as informações dos
    funcionários que atuam no setor de entrada; caso não haja funcionários
    atuando no setor, retorna uma lista vazia string,list(list)->list(list)'''
    
    final=[]
    
    for linha in matriz:
        if setor in linha:
            list.append(final,linha)
    
    for informacoes in final:
        list.remove(informacoes,setor)
    
    return final