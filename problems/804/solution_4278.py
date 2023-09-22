#Start your python function here
def filtra_pares(a, b, c, d):
    x = [a, b, c, d]
    y = (a, b, c, d)
    if y % 2 == 0:
        return True
    else: 
        return False 
    list(filter(x, y))