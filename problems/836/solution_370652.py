def busca(setor,matriz):
    """ funcão que recebe como entrada uma matriz com :nome,registro
    ,setor e telefone, de cada funcionario; e um setor a ser 
    buscado, retorna todos os funcionarios do setor procurado.
    entrada->str,list(list)
    saida->list(list) """
    lista=[]
    
    for i in matriz:
        if i[2] == setor:
            i.remove(setor)
            lista.append(i)
                      
    return lista