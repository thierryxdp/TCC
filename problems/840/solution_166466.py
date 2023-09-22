def qtd_bolos(a,b,c):
    " Cálcula a quantidade de bolos, possíveis int, int - > int "
    " Dividide pela qtd necessária por ingrediente "
    xicaras = a //2
    ovos = b // 3
    leite = c // 5
    " Pega o minimo, será o fator determinante "
    minimo = min(xicaras,ovos,leite)
    " Retorna a quantidade de bolos, possíveis "
    return minimo