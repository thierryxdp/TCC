#Start your python function here
import math
def filtra_pares (a,b,c,d):
    if (a%2==0 and b%!=0 and c%!=0 and d%!=0):
        return a
    elif (a%2==0 and b%==0 and c%!=0 and d%!=0):
        return a, b
    elif (a%2==0 and b%==0 and c%==0 and d%!=0):
        return a, b, c
    elif (a%2==0 and b%==0 and c%!=0 and d%!=0):
        return a, b, c, d
    elif (a%2==0 and b%!=0 and c%==0 and d%!=0):
        return a, c
    elif (a%2==0 and b%!=0 and c%==0 and d%==0):
        return a, c,d