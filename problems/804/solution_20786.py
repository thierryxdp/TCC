def filtra_pares(tupla):
    '''funcao que filtra uma yupla retornando apenas
os valores pares; tup(int,int,int,int) -> tup''' 
    if tupla[0]%2 == 0:
        situacao1 = tupla[0]
    else:
        situacao1 = ()    
    if tupla[1]%2 == 0:
        situacao2 = tupla[1]
    else:
        situacao2 = ()
    if tupla[2]%2 == 0:
        situacao3 = tupla[2]
    else:
        situacao3 =()
    if tupla[3]%2 == 0:
        situacao4 = tupla[3]
    else:
        situacao4 = ()
    return (situacao1,situacao2,situacao3,situacao4)