#Start your python function here
def filtra_pares(num):
    num2 = ()
    if num[0]%2 == 0:
        num2 += (num[0],)
        
    if num[1]%2 == 0:
        num2 += (num[1],)
        
    if num[2]%2 == 0:
        num2 += (num[2],)
        
    if num[3]%2 == 0:
        num2 += (num[3],)
        
    return num2