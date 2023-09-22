#Start your python function here
def filtra_pares(a):
    if(a[0]%2==0) and (a[1]%2==0) and (a[2]%2==0) and (a[3]%2==0) :
    	return a
    elif(a[0]%2==0) and (a[1]%2!=0) and (a[2]%2!=0) and (a[3]%2!=0):
        return a[0]
    elif(a[0]%2!=0) and (a[1]%2==0) and (a[2]%2!=0) and (a[3]%2!=0):
        return a[1]
    elif(a[0]%21!=0) and (a[1]%2!=0) and (a[2]%2==0) and (a[3]%2!=0):
        return a[2]
    elif(a[0]%21!=0) and (a[1]%2!=0) and (a[2]%2!=0) and (a[3]%2==0):
        return a[3]
    elif(a[0]%21==0) and (a[1]%2==0) and (a[2]%2!=0) and (a[3]%2!=0):
        return a[0], a[1]
     else:
        return "ok"