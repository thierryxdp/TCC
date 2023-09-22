#Start your python function here
def filtra_pares(x):
    s=()
    if x[0]% 2==0:
        s+=(x[0],)
    if x[1]% 2==0:
        s+=(x[1],)
    if x[2]% 2==0:
        s+=(x[2],)
    if x[3]% 2==0:
        s+=(x[3],)   
    return s