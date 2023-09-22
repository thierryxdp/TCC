#list(int)->tuple
def melhor_volta(tempos):
    "Funçao que retorna um tupla,de quem foi a melhor volta da prova, com qual tempo e em que volta."
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if tempos[i][j] < tupla[1]:
                tupla = (i+1,tempos[i][j],j+1)
    return tupla