#Start your python function here
def filtra_pares(R):
    #essa função retornará uma tupla com os números pares
    J = ()
    #logo abaixo, foi feito uma seleção individual, se o resto for 0, logicamente ele será par
    if R[0] % 2 == 0:
        J = J + (R[0],)
    if R[1] % 2 == 0:
        J = J + (R[1],)
    if R[2] % 2 == 0:
        J = J + (R[2],)
    if R[3] % 2 == 0:
        J = J + (R[3],)
    return J