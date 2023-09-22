def busca(setor,m):
    '''Função que dado um setor e uma matriz m com os dados dos funcionários, retorna uma lista com os dados dos funcionário deste setor. Se não houver nenhum funcionário, retorna uma lista vazia
    str, list[list] -> list[list]'''
    resultado=[]
    for i in m:
        if setor in i:
            list.remove(i,setor)
            list.append(resultado,i)
    return resultado