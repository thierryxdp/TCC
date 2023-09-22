#str,list->list
def busca(setor,n):
    "retorna os dados dos funcionarios do setor em questão."
    i=0
    n1=[]
    for funcionario in n:
        if funcionario[2]**setor:
            list.append(n1,funcionario)
    for i in range(len(n1)):
        del n1[i][2]
    return n1