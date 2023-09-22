def melhor_volta(l):
    """Verifica a melhor volta entre todos os pilotos, retornando qual piloto fez essa melhor volta,
    o tempo da melhor volta e em qual das voltas esse tempo foi obtido
    input: l -> list
    melhores_voltas -> list
    melhor_volta -> int
    melhor_volta_geral -> int
    piloto -> int
    nr_volta -> int
    output: tuple
    """
    melhores_voltas = []
    for i in range(len(l)):
        melhor_volta = min(l[i])
        melhores_voltas.append(melhor_volta)
    melhor_volta_geral = min(melhores_voltas)
    piloto = melhores_voltas.index(melhor_volta_geral) + 1
    nr_volta = l[piloto - 1].index(melhor_volta_geral) + 1
    return piloto, melhor_volta_geral, nr_volta