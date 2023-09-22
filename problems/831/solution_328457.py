def lingua_p(L):
    A = 'apa'
    E = 'epe'
    I = 'ipi'
    O = 'opo'
    U = 'upu'
    F = L.replace(A,'a')
    F = L.replace(E,'e')
    F = L.replace(I,'i')
    F = L.replace(O,'o')
    F = L.replace(U,'u')
    return F