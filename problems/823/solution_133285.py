def faltante(listaFaltante):
    listaFaltante.sort()	
    n = max(listaFaltante)
    listaCorreta = list(range(1, n+1))
    i = 0
    while i < len(listaFaltante):
        if(listaFaltante[i] != listaCorreta[i]):
            return listaCorreta[i]
        i += 1
    return listaFaltante.pop() + 1