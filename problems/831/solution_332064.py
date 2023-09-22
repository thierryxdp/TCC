def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """  
    nova_palavra = palavra
    for letra in palavra:
        
        if letra in'a':
            nova_palavra = str.replace(nova_palavra,'a','apa',1)
       
        elif letra in'e':
            nova_palavra = str.replace(nova_palavra,'e','epe',1)
       
        elif letra in'i':
            nova_palavra = str.replace(nova_palavra,'i','ipi',1)
      
        elif letra in'o':
            nova_palavra = str.replace(nova_palavra,'o','opo',1)
       
        elif letra in'u':
            nova_palavra = str.replace(nova_palavra,'u','upu',1)
        
        elif letra not in 'aeiou':
            nova_palavra = nova_palavra
       
                                 
    return nova_palavra