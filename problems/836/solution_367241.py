#5
#str,list(list)->list
def busca(setor,matriz):
    "Função que dado um nome de um setor da empresa e uma matriz, a função retorna os dados de todos os funcionários daquele setor."
    lista=[]
    for i in range(0,3):
        if setor in matriz[i]:
            del matriz[i][2]
            list.append(lista,matriz[i])
    return lista