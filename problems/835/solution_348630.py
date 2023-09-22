def melhor_volta(matriz):
    '''avalia e retorna de quem foi a melhor volta, com
    que tempo e em que volta dentre 60 voltas, 
    10 de cada corredor;
    list -> tuple'''
    voltas=[]
    for corredor in matriz:
        for volta in corredor:
            voltas+=[volta]
    minimo=min(voltas)
    i=voltas.index(minimo)
    quem=i//10 +1
    qvolta=i%10+1
    return 'corredor '+str(quem),minimo,qvolta