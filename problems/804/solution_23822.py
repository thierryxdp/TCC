#Start your python function here
def filtra_pares(tupla):
    """Recebe um tupla com quatro elementos e retorna em mesma ordem apenas
    os que sao pares;
    int[4] --> int[?]"""
    buffer = ()

    if n_par(tupla[0]):
        buffer = buffer + tupla[0:1]

    if n_par(tupla[1]):
        buffer = buffer + tupla[1:2]

    if n_par(tupla[2]):
        buffer = buffer + tupla[2:3]

    if n_par(tupla[3]):
        buffer = buffer + tupla[3:]

    return buffer