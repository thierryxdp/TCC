def filtra_pares(x):
      """função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elemtnos pares da primeira tupla"""
         
        a=[0]
        b=[1]
        c=[2]
        d=[3]
        
        tupla_final = ()
        if a%2!==0:
            tupla_final= tupla_final + (a,)
        if b%2!==0:
            tupla_final= tupla_final + (b,)
        if c%2!==0:
            tupla_final= tupla_final + (c,)
        if d%2!==0:
            tupla_final= tupla_final + (d,)
            
            return tupla_final