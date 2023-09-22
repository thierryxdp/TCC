def filtra_pares(elementos):
    # A função recebe uma lista com elementos, verificada para cada elemento se o mesmo é par
    # caso seja par adiciona-o a uma tupla, caso não verifica o próximo, até o fim da lista.
    # list-> tuple
    tupla_par=tuple()
    x=0
    for numero in elementos:
        if numero%2==0:
			tupla_par+=tuple(elementos[x:x+1])
		x+=1
    return tupla_par