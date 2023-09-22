def colisao(a, b):
    a1=a[0]
    a2=a[1]
    a3=a[2]
    a4=a[3]

    b1=b[0]
    b2=b[1]
    b3=b[2]
    b4=b[3]

    if (a3 < b1 and a4 < b2 or b3 < a1 and b4 < a2 ):
         return "False"
    else:
        return "True"