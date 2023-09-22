def melhor_volta(matriz):
    lista=[]
    listax=[]
    menores=[]
    mini= 0
    n_ls=0
    n_cs=0
    for menores in matriz:
        listax+=[min(menores)]
    mini=min(listax)
    for linhas in matriz:
        n_ls+=1
        if mini in linhas:
            for colunas in linhas:
                n_cs+=1
                if mini==colunas:
                    break
        	return (n_ls, mini, n_cs)