def filtra_pares ( a1, a2, a3, a4):

    if a1%2==0 and a2%2==0 and a3%2==0 and a4%2==0:
        return print(a1,a2,a3,a4)
    elif a1%2!=0 and a2%2==0 and a3%2==0 and a4%2==0:
        return print(a2,a3,a4)
    elif a1%2==0 and a2%2!=0 and a3%2==0 and a4%2==0:
        return print(a1,a3,a4)
    elif a1%2==0 and a2%2==0 and a3%2!=0 and a4%2==0:
        return print(a1,a2,a4)
    elif a1%2==0 and a2%2==0 and a3%2==0 and a4%2!=0:
        return print(a1,a2,a3)
    elif a1%2!=0 and a2%2!=0 and a3%2==0 and a4%2==0:
        return print(a3,a4)
    elif a1%2!=0 and a2%2==0 and a3%2!=0 and a4%2==0:
        return print(a2,a4)
    elif a1%2!=0 and a2%2==0 and a3%2==0 and a4%2!=0:
        return print(a2,a3)
    elif a1%2==0 and a2%2!=0 and a3%2!=0 and a4%2==0:
        return print(a1,a4)
    elif a1%2==0 and a2%2!=0 and a3%2==0 and a4%2!=0:
        return print(a1,a3)
    elif a1%2==0 and a2%2==0 and a3%2!=0 and a4%2!=0:
        return print(a1,a2)
    elif a1%2!=0 and a2%2!=0 and a3%2!=0 and a4%2==0:
        return print(a4)
    elif a1%2!=0 and a2%2!=0 and a3%2==0 and a4%2!=0:
        return print(a3)
    elif a1%2==0 and a2%2!=0 and a3%2!=0 and a4%2!=0:
        return print(a1)
    elif a1%2!=0 and a2%2==0 and a3%2!=0 and a4%2!=0:
        return print(a2)
    else:
        return ''