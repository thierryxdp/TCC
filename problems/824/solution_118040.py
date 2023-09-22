def filtraMultiplos(lista,n):
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo] / n == 0:
            multiplos = multiplos + (lista[proximo],)
        proximo = proximo + 1
    return multiplos

def uppCons(frase):
    consoantes = ()
    proximaLetra = 0
    while proximaLetra < len(frase):
        if frase[proximaLetra] != 'AEIOUaeiou':
            consoantes = upper.consoantes + frase
        proximaLetra = proximaLetra + 1
    return consoantes