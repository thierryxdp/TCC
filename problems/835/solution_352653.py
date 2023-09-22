def melhor_volta(M):
    '''Função que dada uma matriz M onde as seis linhas 
correspondem aos corredores e as 10 colunas, às voltas, e
retorna de quem foi a melhor volta da prova, com qual tempo
e em que tempo;
	list -> tupla'''
    n=[]
    for i in range(len(M)):
        #for j in range(len(M[i])):
        n=n+min(M[i])
    m=min(n)
    return i+1,m,list.index(n,m)+1