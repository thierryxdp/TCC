#Start your python function here
def filtra_pares(tuple):
    tuple1=()
    if tuple[0]%2==0:
        tuple1=tuple1+ (tuple[0],)
    if tuple[1]%2==0:
        tuple1=tuple1+(tuple[0,1],)
    if tuple[2]%2==0:
        tuple1=tuple1+(tuple[0,1,2],)
    if tuple[3]%2==0:
        tuple1=tuple1+(tuple[0,1,2,3],)
        return tuple1