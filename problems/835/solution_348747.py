def melhor_volta(lista):
    resultado = 0
    for i in range(len(lista)):
            resultado = resultado+ min(lista[i])
            return resultado