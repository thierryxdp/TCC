def busca (setor,matriz):
    '''retorna os dados de todos os funcionários
    do setor. 
    string, lista-> lista'''
    
    inf = []
    i = 0
    
    for linhas in matriz: 
        for elementos in linhas:
            if setor == elementos: 
                inf = inf + [del.matriz[i][2]]