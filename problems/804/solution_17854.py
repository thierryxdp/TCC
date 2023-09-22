def filtra_pares(elementos):
    '''
    	Funcao que recebe uma tupla com quatro elementos 
        inteiros e retorna uma nova tupla contendo apenas
        os elementos pares da tupla original
        tupla -> tupla
    '''
    a = elementos[0]
    b = elementos[1]
    c = elementos[2]
    d = elementos[3]
    
    # elementos
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        elementos = a, b, c, d
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        elementos = b, c, d
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        elementos = a, c, d
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        elementos = a, b, d
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        elementos = a, b, c
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        elemntos = c, d
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        elementos = b, d
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        elementos = b, c
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        elementos = b
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        elementos = c
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        elementos = d
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        elementos = a
    else:
        return "()"
    return "(" + elementos + ",)"