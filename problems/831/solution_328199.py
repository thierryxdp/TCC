def lingua_p(palavra):
    
    for letra in ('a','e','i','o','u'):
      
       if letra in palavra :
               palavra+=letra +'p'+letra  
           ##            print (palavra)
    return palavra