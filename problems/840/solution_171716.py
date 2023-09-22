def bolos(xicaras,ovos,leite):
'int,int,int -> int; Cálculo para quantidade de bolos possíveis.'
    import math
    return math.floor(min(xicaras/2,ovos/3,leite/5))