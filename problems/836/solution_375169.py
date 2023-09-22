def busca(setor,matriz):
    '''Dado um setor e uma matriz, a função deve retornar
    todas os dados dos funcionários daquele setor;
    str, list(list)->list(list)'''
    
    funcionarios_do_setor=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j]==setor):
                list.append(funcionarios_do_setor,matriz[i])
                if(True):
                    list.remove(funcionarios_do_setor,setor)
    return(funcionarios_do_setor)