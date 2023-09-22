def busca(setor,matriz):
    '''função que retorna em uma lista o setor procurado 
    dentro de uma matriz
    string,list(list)->list(list)'''
    lista_busca=[]
    for linha in matriz:
        if linha[2]==setor:
            del(linha[2])
            lista_busca.append(linha)
    return lista_busca