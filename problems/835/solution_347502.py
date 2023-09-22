def melhor_volta(tempos):
    """função que recebe como entrada uma matriz 6x10 com os tempos em 
       segundos dos corredores em cada volta, e retorna uma tupla 
       informando de qual corredor foi a melhor volta da prova e com qual 
       tempo e em que volta.
       list -> tuple
       
       Parâmetros:
       tempos: Uma matriz 6x10 com os tempos de cada um dos corredores em 
               suas respectivas voltas.
       
       Returns: Uma tupla informando de qual corredor foi a melhor volta 
                da prova e com qual tempo e em que volta.
    """
    menortempo = (0,999999,)
    for corredores in range(len(tempos)):
        for voltas in range(len(tempos[0])):
            if tempos[corredores][voltas] < menortempo[1]:
                menortempo = (corredores+1,tempos[corredores][voltas],voltas+1)
    return menortempo