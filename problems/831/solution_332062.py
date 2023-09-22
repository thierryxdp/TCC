def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """  
    nova_palavra = palavra
    for letra in palavra:
        
        if letra =='a':
            nova_palavra = str.replace(palavra,'a','apa',1)
       
        if letra =='e':
            nova_palavra = str.replace(palavra,'e','epe',1)
       
        if letra =='i':
            nova_palavra = str.replace(palavra,'i','ipi',1)
      
        if letra =='o':
            nova_palavra = str.replace(palavra,'o','opo',1)
       
        if letra =='u':
            nova_palavra = str.replace(palavra,'u','upu',1)
        
        if letra not in 'aeiou':
            nova_palavra = nova_palavra
       
                                 
    return nova_palavra