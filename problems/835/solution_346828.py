def melhor_volta(resultado):
    """Funcao que recebe como entrada uma matriz 6X10 com os tempos segundos
    dos corredores em cada volta e retorna uma tupla informando quem teve a
    melhor volta, com qual tempo e em que volta"""
    melhor_volta = []
    for corredor in resultado:
        list.append(melhor_volta,min(corredor))
    b = min(melhor_volta)
    a = list.index(melhor_volta, b)
    c = list.index(resultado[a],b)
    return (a+1,b,c+1)