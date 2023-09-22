#str,list->list
def busca(setor,matriz):
    "retorna os dados dos funcionarios do setor em questão."
    i=0
    matriz1=[]
    for funcionario in matriz:
        if funcionario[2]**setor:
            list.append(matriz1,funcionario)
    for i in range(len(nmatriz1)):
        del matriz1[i][2]
    return matriz1