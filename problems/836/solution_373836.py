def busca(setor,matriz):
    '''função que recebe uma matriz e faz uma busca por setor, ou seja, dado um nome de um setor em string da empresa, a função retorna os dados de todos os funcionários daquele setor; str, list (mat) -> list'''
    contato=[]
    for i in matriz:
        if setor in i:
            i=[i[0],i[1],i[3]]
            contato+= [i]
        else:
            contato+=[]
    return contato