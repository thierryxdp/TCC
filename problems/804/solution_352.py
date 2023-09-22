# Retorna uma tupla com somente os numeros pares
# int,int,int,int-> tupla
def filtra_pares(s):
    x = s[0]%2
    y = s[1]%2
    w = s[2]%2
    z = s[3]%2
    if x==0 and y==0 and w==0 and z==0:
        return (s[0],s[1],s[2],s[3])
    elif x==0 and y==0 and w==0:
        return (s[0],s[1],s[2])
    elif x==0 and y==0 and z==0:
        return (s[0],s[1],s[3])
    elif x==0 and w==0 and z==0:
        return (s[0],s[2],s[3])
    elif y==0 and w==0 and z==0:
        return (s[1],s[2],s[3])
    elif x==0 and y==0:
        return (s[0],s[1])
    elif x==0 and w==0:
        return (s[0],s[2])
    elif x==0 and z==0:
        return (s[0],s[3])
    elif y==0 and w==0:
        return (s[1],s[2])
    elif y==0 and z==0:
        return (s[1],s[3])
    elif w==0 and z==0:
        return (s[2],s[3])
    elif x==0:
        return (s[0],)
    elif y==0:
        return (s[1],)
    elif w==0:
        return (s[2],)
    elif z==0:
        return (s[3],)
    else:
        return()