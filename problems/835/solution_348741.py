def melhor_volta(lista):
    resultado = ()
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            resultado = resultado+ min(lista[i])
            return resultado