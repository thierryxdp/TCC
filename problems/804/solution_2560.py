def filtra_pares(tupla):
    """Recebe uma tupla com quatro elementos e retorna só os elementos pares, na mesma ordem
    Entrada: tuple de int
    Saída: tuple de int"""
    
    a0,a1,a2,a3=tupla[0]%2,tupla[1]%2,tupla[2]%2,tupla[3]%2
    
    if a0==0 and a1==0 and a2==0 and a3==0:
        return tupla[0],tupla[1],tupla[2],tupla[3]
    
    elif a0!=0 and a1==0 and a2==0 and a3==0:
        return tupla[1],tupla[2],tupla[3]
    
    elif a0==0 and a1!=0 and a2==0 and a3==0:
        return tupla[0],tupla[2],tupla[3]
    
    elif a0==0 and a1==0 and a2!=0 and a3==0:
        return tupla[0],tupla[1],tupla[3]
    
    elif a0==0 and a1==0 and a2==0 and a3!=0:
        return tupla[0],tupla[1],tupla[2]
    
    elif a0!=0 and a1!=0 and a2==0 and a3==0:
        return tupla[2],tupla[3]
    
    elif a0==0 and a1!=0 and a2!=0 and a3==0:
        return tupla[0],tupla[3]
    
    elif a0==0 and a1==0 and a2!=0 and a3!=0:
        return tupla[0],tupla[1]
    
    elif a0!=0 and a1==0 and a2==0 and a3!=0:
        return tupla[1],tupla[2]
    
    elif a0!=0 and a1==0 and a2!=0 and a3==0:
        return tupla[1],tupla[3]
   	
    elif a0==0 and a1!=0 and a2==0 and a3!=0:
        return tupla[0],tupla[2]
    
    elif a0==0 and a1!=0 and a2!=0 and a3!=0:
        return tupla[0],
    elif a0!=0 and a1==0 and a2!=0 and a3!=0:
        return tupla[1],
    elif a0!=0 and a1!=0 and a2==0 and a3!=0:
        return tupla[2],
    elif a0!=0 and a1!=0 and a2!=0 and a3==0:
        return tupla[3],
    else:
        return ()
    
#Start your python function here