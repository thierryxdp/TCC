def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """
    
    
    
    
    
    if 'a' in palavra:
        palavra = str.replace(palavra,'a','apa')
    elif 'e' in palavra:
        palavra = str.replace(palavra,'e','epe')
    elif 'i' in palavra:
        palavra = str.replace(palavra,'i','ipi')
    elif 'o' in palavra:
        palavra = str.replace(palavra,'o','opo')
    elif 'u' in palavra:
        palavra = str.replace(palavra,'u','upu')
       
            
            
    return palavra