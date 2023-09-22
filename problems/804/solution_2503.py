#Start your python function here
def filtra_pares(tupl):
    n0,n1,n2,n3 = tupl
    par_tupl = ()
    
    if n0/2 == float(n0//2):
        par_tupl += (tupl[0],)
    if n1/2 == float(n1//2):
        par_tupl += (tupl[1],)

    if n2/2 == float(n2//2):
        par_tupl += (tupl[2],)
    return par_tupl

    if n3/2 == float(n3//2):
        par_tupl += (tupl[3],)