#Start your python function here
def filtra_pares(a):
    i=()
    if a[0]%2==0:
        i=a[0]
    if a[1]%2==0:
        i=i , a[1]
    if a[2]%2==0:
        i=i ,a[2]
    if a[3]%2==0:
        i= i , a[3]
        
        return i