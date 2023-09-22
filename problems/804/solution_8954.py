#Start your python function here
def filtra_pares(tupla):
    tupla1=()
    if tupla[0]%2==0:
        tupla_1=tupla1+tupla[0]
        return tupla_1
    elif tupla[1]:
         tupla_1=tupla1+tupla[1]
        return tupla_1
    elif tupla[2]:
         tupla_1=tupla1+tupla[2]
        return tupla_1
    elif tupla[3]:
         tupla_1=tupla1+tupla[3]
        return tupla_1
    elif tupla[0]%2==0 and tupla[1]%2==0:
        tupla_2=tupla1+tupla[0]+tupla[1]
        return tupla_2
    elif tupla[0]%2==0 and tupla[2]%2==0:
        tupla_2=tupla1+tupla[0]+tupla[2]
        return tupla_2
    elif tupla[0]%2==0 and tupla[3]%2==0:
        tupla_2=tupla1+tupla[0]+tupla[3]
        return tupla_2
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
            tupla_3=tupla_1+tupla[0]+tupla[2]+tupla[3]
            return tupla_3
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
            tupla_3=tupla_1+tupla[0]+tupla[2]+tupla[3]
            return tupla_3