#Start your python function here
def filtra_pares(a, b, c, d):
    def par(n):
        if n % 2 == 0:
            return True
        else:
            return False
        list(filter(par,filtra_pares))