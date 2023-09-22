def multiplo(m, n):

        if m%n == 0:

                return n

        return None

def filtraMultiplos(lista, n):

        multiplo = lambda m: m%n == 0 

        saida = list(filter(multiplo, lista))

        return saida