def maiores(ls, n): # satisfaz todos os testes
    cp = ls[:] + [n] # agora tenho certeza que n in cp
    list.sort(cp) # cp ordenada
    pri = list.index(cp, n) # posição da primeira occorrência de n
    return cp[pri + 1: ]