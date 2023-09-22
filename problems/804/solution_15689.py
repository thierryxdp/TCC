#tupla, int->tupla, int
def filtra_pares(a,b,c,d):
    num=(a,b,c,d)
    if num[0]%2==0 and num[1]%2==0 and num[2]%2==0 and num[3]%2==0:
        return num[0:4]
    elif num[0]%2==0 and num[1]%2!=0 and num[2]%2!=0 and num[3]%2!=0:
        return num[0]
    elif num[0]%2==0 and num[1]%2==0 and num[2]%2!=0 and num[3]%2!=0:
        return num[:2]
    elif num[0]%2==0 and num[1]%2==0 and num[2]%2==0 and num[3]%2!=0:
        return num[:3]