def busca(setor,matriz):
    '''Função que recebe uma matriz contendo os dados dos funcionários de uma empresa e uma string com um setor da empresa e a função fará uma busca e retornará uma lista com os dados de todos os funcionários do setor buscado.
       parâmetro de entrada:str,list
       valor de retorno:list'''
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista,matriz[i])
            list.remove(matriz[i],setor)
    return lista