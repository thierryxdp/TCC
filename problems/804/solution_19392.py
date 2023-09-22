#Start your python function here
def pares(t):
    if not t:
        return 0            
    return (t[0] % 2 == 0) + pares(t[1:])