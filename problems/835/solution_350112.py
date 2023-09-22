def melhor_volta(matriz):
    '''Função que ao receber uma matriz 6x10 com os tempos 
    em segundos dos corredores retorna uma tupla informando
    de quem foi a melhor volta com o seu respectivo tempo
    e em qual volta teve o melhor tempo.
    list ->tuple'''
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