def filtra_pares (a):
    ''' função que receba uma tupla com quatro elemetos inteiros e retorne uma nova tupla '''
    b= ()
        if a[0] % 2 == 0:
             b = b + (a[1],)
                
        if a[1] % 2 == 0:
             b = b + (a[1],) 
           
   
        if a[2]% 2 == 0:
              b = b+ (a[2],)
            
        if a[3]% 2 == 0 :
            b = b + (a[3],)
            return b