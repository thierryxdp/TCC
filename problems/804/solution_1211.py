#Start your python function here
def filtra_pares(tupla):
    """Para filtrar os núemeros pares da tupla, digite;
    tupla-> int"""
    r1=tupla[0]%2
    r2=tupla[1]%2
    r3=tupla[2]%2
    r4=tupla[3]%2
    if r1==0 and r2==0 anda r3==0 and r4==0:
        return tupla