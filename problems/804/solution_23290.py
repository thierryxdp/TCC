def filtra_pares(s):
    n1=s[0]
    n2=s[1]
    n3=s[2]
    n4=s[3]
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return tuple(s)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2==0:
        return tuple(s[:1])
     elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2==0:
            return tuple(s[:2])
        elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
            return tuple(s[:3])
        elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
            return tuple(s[:4])