def eh_par(n):
    """Diz se n é par."""
    return n % 2 == 0
# Casos de teste
# eh_par(2) == True
# eh_par(1) == False
# eh_par(0) == True

def filtra_pares(t):
    """Verifica cada elemento t[i] da tupla t.  Se
    t[i] é par, cria uma NOVA tupla concatenando 
    a antiga tupla que tínhamos com uma nova contendo
    apenas o número t[i] em questão."""
    ret = ()
    if eh_par(t[0]):
        ret = ret + (t[0], )
    if eh_par(t[1]):
        ret = ret + (t[1], )
    if eh_par(t[2]):
        ret = ret + (t[2], )
    if eh_par(t[3]):
        ret = ret + (t[3], )
    return ret