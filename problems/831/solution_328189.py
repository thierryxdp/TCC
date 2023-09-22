def lingua_p(palavra):
    
    for letra in palavra:
       palavra+=letra +'p'+letra
       if letra in('a','e','i','o','u') :
                 palavra+=letra +'p'+letra
           ##            print (palavra)
    return (palavra)