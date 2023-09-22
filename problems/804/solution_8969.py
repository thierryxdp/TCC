#Start your python function here
def filtra_pares(tupla):
    """função que recebe uma tupla com quatro elementos inteiros como 
    parametro, e retorne uma nova tupla contendo apenas os elementos
    pares da tupla original na mesma ordem de contagem
    parametro de entrada:tuple
    valor de saida:tuple
    """
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
        return (tupla[0],tupla[1],tupla[2])
    elif tupla[0]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[2],tupla[3]) 
    elif tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[1],tupla[2],tupla[3])
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[1],tupla[3])
    
    elif tupla[0]%2==0 and tupla[1]%2==0:
        return (tupla[0],tupla[1])
    elif tupla[0]%2==0 and tupla[2]%2==0:
        return (tupla[0],tupla[2])
    elif tupla[0]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[3])
    elif tupla[1]%2==0 and tupla[2]%2==0:
        return (tupla[1],tupla[2])
    elif tupla[1]%2==0 and tupla[3]%2==0:
        return (tupla[1],tupla[3])
    elif tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[2],tupla[3])
	elif tupla[0]%2==0:
        return (tupla[0],)
    elif tupla[1]%2==0:
        return (tupla[1],)
    elif tupla[2]%2==0:
        return (tupla[2],)
    elif tupla[3]%2==0:
        return (tupla[3],)
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        return ()