def busca(setor,matriz):
    """Essa função receberá como um de seus parâmetros de 
    entrada uma matriz, sendo que ela conterá as seguintes 
    informações sobre os funcionários de uma empresa: o nome
    deles, registro, setor onde trabalham e número de telefo-
    ne. O outro parâmetro será uma string indicando um setor
    da empresa. Posto isso, essa função fará uma busca, tendo
    como base o setor indicado e retornará os dados de todos
    os funcionários que trabalham naquele setor.
    
    list, str -> list
    """
    
    ret = []
    for i in range(len(matriz)):
        for j in matriz[i]:
            if setor in matriz[i]:
                n = matriz[i]
                del n[2]
                list.append(ret,n)
    return ret