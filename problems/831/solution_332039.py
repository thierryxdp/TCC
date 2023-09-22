def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """
    
    
    contador = 0
    
    while contador <= len(palavra) - 1:
        if 'a' in palavra[contador]:
            palavra = str.replace(palavra[contador],'a','apa')
        
        elif 'e' in palavra[contador]:
            palavra = str.replace(palavra[contador],'e','epe')
        
        elif 'i' in palavra[contador]:
            palavra = str.replace(palavra[contador],'i','ipi')
       
        elif 'o' in palavra[contador]:
            palavra = str.replace(palavra[contador],'o','opo')
        
        elif 'u' in palavra[contador]:
            palavra = str.replace(palavra[contador],'u','upu')
       
            
            
    return palavra