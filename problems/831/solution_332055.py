def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """  
   
    for letra in palavra:
        
       if letra =='a':
            str.replace(palavra,'a','apa',1)
       
       if letra =='e':
            str.replace(palavra,'e','epe',1)
       
       if letra =='i':
            str.replace(palavra,'i','ipi',1)
      
       if letra =='o':
            str.replace(palavra,'o','opo',1)
       
       if letra =='u':
            str.replace(palavra,'u','upu',1)
       
                                 
    return palavra