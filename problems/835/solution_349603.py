def melhor_volta(matriz):
    "Função que recebe uma matriz 6 x 10 com os tempos em segundos dos seis concorrentes em 10 voltas numa pista de Kart, e retorna de quem foi a melhor volta e em qual tempo."
    "list -> tuple"
    voltas = []
    for competidor in matriz:
        for volta in competidor:
            voltas+=[volta]
    k = min(voltas)
    a = voltas.index(k)
    pessoa = a//10 + 1
    p_volta = a%10 +1
    return pessoa, k, p_volta