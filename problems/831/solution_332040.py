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
            palavra = str.replace(palavra,palavra[contador],'epe')
        
        elif 'i' in palavra[contador]:
            palavra = str.replace(palavra,palavra[contador],'ipi')
       
        elif 'o' in palavra[contador]:
            palavra = str.replace(palavra,palavra[contador],'opo')
        
        elif 'u' in palavra[contador]:
            palavra = str.replace(palavra,palavra[contador],'upu')
       
            
            
    return palavra