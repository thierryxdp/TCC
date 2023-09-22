def melhor_volta(M):
    '''Função que dada uma matriz M onde as seis linhas 
correspondem aos corredores e as 10 colunas, às voltas, e
retorna de quem foi a melhor volta da prova, com qual tempo
e em que tempo;
    list -> tupla'''
    n=[]
    p=1000
    for i in range(len(M)):
        list.append(n,min(M[i]))
        for j in range(len(M[i])):
			if M[i][j] < p:
                p=M[i][j]
                j2=j
    m=min(n)
    return list.index(n,m)+1,m,j2+1