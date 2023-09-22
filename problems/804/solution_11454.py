def filtra_pares (tupla):
    tupla_resposta = ()
    if tupla [0] % 2 == 0:
        tupla_resposta += (tupla[0],)
    if tupla [1] % 2 ==0:
        tupla_resposta += (tupla[1],)
    if tupla [2] % 2 == 0:
        tupla_resposta += (tupla[2], )
    if tupla [3] % 2 == 0:
        tupla_resposta += (tupla[3])
    return tupla_resposta