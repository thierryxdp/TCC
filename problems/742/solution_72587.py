# a funcao usa o comando return pra retonar os valores concatenados das strings s,x,i

def substitui(sol, w, p):
    sol[p] = w
    return sol[0:p] + w + sol[p + 1:]