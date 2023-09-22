def melhor_volta(T):
    '''funcao que, dada uma matriz T com os tempos em segundos dos 6 competidores em
    cada uma das 10 voltas, retorna de quem foi a melhor volta, o tempo dessa melhor
    volta e em que volta ela ocorreu;
    matriz -> tuple(int,int,int)'''
    tempos=[]
    for competidor in range(len(T)):
        for tempo in T[competidor]:
            list.append(tempos,tempo)
    menor=min(tempos)
    for competidor in range(len(T)):
        for volta in range(len(T[competidor])):
            if T[competidor][volta]==menor:
                return (competidor,menor,volta)