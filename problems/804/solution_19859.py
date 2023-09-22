def filtra_pares(x):
    '''Função que recebe 4 elementos inteiros x=(a,b,c,d) e
    retorna uma nova sequência (tupla) contendo apenas os
    elementos pares da tubla original, mantendo a ordem;
    	tupla (int,int,int,int) -> tupla(int,int,int,int)'''
    	a=int(x[0])
        b=int(x[1])
        c=int(x[2])
        d=int(x[3])
        if(a%2==0 and b%2==0 and c%2==0 and d%2==0):
            return str(a),str(b),str(c),str(d)
        elif(a%2==0 and b%2==0 and c%2==0 and d%2!=0):
            return str(a),str(b),str(c)
        elif(a%2==0 and b%2==0 and c%2!=0 and d%2==0):
            return str(a),str(b),str(d)
        elif(a%2==0 and b%2!=0 and c%2==0 and d%2==0):
            return str(a),str(c),str(d)
        elif(a%2==0 and b%2==0 and c%2!=0 and d%2!=0):
            return str(a),str(b)
        elif(a%2==0 and b%2!=0 and c%2==0 and d%2!=0):
            return str(a),str(c)
        elif(a%2==0 and b%2!=0 and c%2!=0 and d%2==0):
            return str(a),str(d)
        elif(a%2==0 and b%2!=0 and c%2!=0 and d%2!=0):
            return str(a)
        elif(a%2!=0 and b%2==0 and c%2==0 and d%2==0):
            return str(b),str(c),str(d)
        elif(a%2!=0 and b%2==0 and c%2==0 and d%2!=0):
            return str(b),str(c)
        elif(a%2!=0 and b%2==0 and c%2!=0 and d%2==0):
            return str(b),str(d)
        elif(a%2!=0 and b%2==0 and c%2!=0 and d%2!=0):
            return str(b)
        elif(a%2!=0 and b%2!=0 and c%2==0 and d%2==0):
            return str(c),str(d)
        elif(a%2!=0 and b%2!=0 and c%2==0 and d%2!=0):
            return str(c)
        elif(a%2!=0 and b%2!=0 and c%2!=0 and d%2==0):
            return str(d)