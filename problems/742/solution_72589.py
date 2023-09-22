def substitui(sol, w, p):
    sol[p] = w
    return sol[0:4] + w + sol[4 + 1:]