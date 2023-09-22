def filtra_pares(a,b,c,d):
    tuplavazia=()
    tupla1=(a,b,c,d)
    tupla2=(a,b,c,)
    tupla3=(a,c,d,)
    tupla4=(a,b,d,)
    tupla5=(b,c,d,)
    tupla6=(a,b,)
    tupla7=(a,c,)
    tupla8=(a,d,)
    tupla9=(b,c,)
    tupla10=(b,d)
    tupla11=(c,d)
    tupla12=(a,)
    tupla13=(b,)
    tupla14=(c,)
    tupla15=(d,)
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return tupla1
    if a%2==0 and b%2==0 and c%2==0 and not d%2==0:
        return tupla2
    if a%2==0 and b%2==0 and not c%2==0 and not d%2==0:
        return tupla6
    if a%2==0 and not b%2==0 and not c%2==0 and not d%2==0:
        return tupla12
    if a%2!=0 and b%2==0 and not  c%2==0 and not d%2==0:
        return tupla13
    if a%2!=0 and not b%2==0 and  c%2==0 and not d%2==0:
        return tupla14
    if a%2!=0 and b%2==0 and  c%2==0 and d%2==0:
        return tupla5
    if a%2!=0 and not b%2==0 and  c%2==0 and d%2==0:
        return tupla11
    if a%2!=0 and not b%2==0 and not c%2==0 and d%2==0:
        return tupla15
    if a%2!=0 and not b%2==0 and not c%2==0 and not d%2==0:
        return ()
    if a%2==0 and not b%2==0 and not c%2==0 and d%2==0:
        return tupla8
    if a%2==0 and not b%2==0 and  c%2==0 and not d%2==0:
        return tupla7
    if a%2!=0 and b%2==0 and  c%2==0 and not d%2==0:
        return tupla9
    if a%2!=0 and b%2==0 and not c%2==0 and d%2==0:
        return tupla10
    if a%2==0 and not b%2==0 and c%2==0 and d%2==0:
        return tupla3
    if a%2==0 and  b%2==0 and not c%2==0 and d%2==0:
         return tupla4#Start your python function here