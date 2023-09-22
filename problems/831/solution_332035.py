def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """
    
    
    
    
    
    if 'a' in palavra:
        palavra = str.replace(palavra,letra,'apa')
    elif 'e' in palavra:
        palavra = str.replace(palavra,letra,'epe')
    elif 'i' in palavra:
        palavra = str.replace(palavra,letra,'ipi')
    elif 'o' in palavra:
        palavra = str.replace(palavra,letra,'opo')
    elif 'u' in palavra:
        palavra = str.replace(palavra,letra,'upu')
       
            
            
    return palavra