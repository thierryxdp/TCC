def melhor_volta(m):
    """Função que recebe uma matriz m de 6x10 com os tempos de cada um dos corredores. Retorna uma tupla informando o melhor corredor, a melhor volra e o melhor tempo da prova.List_> tuple"""
    
    l=[]
    for i in range (len(m)):
        for j in range (len(m[0])):
            l=l+[m[i][j]]
    a=min(l)
    b=l.index(a)
    return((int(b/10))+1,a,(int(b%10))+1)