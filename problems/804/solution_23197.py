#Start your python function here
def filtra_pares(t):
    r=()
    if(t[0]%2==0):
        r=r+t[0]
    if(t[1]%2==0):
        r=(r,)+t[1]
    if(t[2]%2==0):
        r=(r,)+t[2]
    if(t[3]%2==0):
        r=(r,)+t[3]
    return r