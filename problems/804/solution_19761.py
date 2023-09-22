def filtra_pares(a,b,c,d):
    """retorne somente os números pares dos elementos de entrada"""
      if ('a'%2==0) and ('b'%2==0) and ('c'%2==0) and ('d'%2==0):
             return (a,b,c,d) 
            elif ('a'%2!=0) and ('b'%2==0) and ('c'%2==0) and ('d'%2==0):
                return (b,c,d)