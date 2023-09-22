def soma_h (numero):
    soma=0
    for corredor in range (numero):
        if corredor == 0:
            soma= soma + 0
        else:
            soma= soma + 1/corredor
    return round (soma + 1/numero,2)