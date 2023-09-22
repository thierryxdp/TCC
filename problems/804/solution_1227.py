#Start your python function here
def filtra_pares(tupla):
    """Para filtrar os núemeros pares da tupla, digite;
    tupla-> int"""
    r1=tupla[0]%2
    r2=tupla[1]%2
    r3=tupla[2]%2
    r4=tupla[3]%2
    
    if r1==0 and r2==0 and r3==0 and r4==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    elif r1==0 and r2==0 and r3==0:
        return (tupla[0],tupla[1],tupla[2])
    elif r1==0 and r2==0 and r3==0:
        return (tupla[0],tupla[1])
    elif r1==0 and r3==0:
        return (tupla[0],tupla[2])
    elif r1==0 and r4==0:
        return (tupla[0],tupla[3])
    elif r2==0 and r3==0:
        return (tupla[1],tupla[2])
    elif r2==0 and r4==0:
        return (tupla[1],tupla[3])
    elif r3==0 and r4==0:
        return (tupla[2],tupla[3])
    elif r3==0 and r4==0:
        return (tupla[2],tupla[3])