def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """
    
    
    
    
    
    if letra in 'a':
        palavra = str.replace(palavra,letra,'apa')
    elif letra in 'e':
        palavra = str.replace(palavra,letra,'epe')
    elif letra in 'i':
        palavra = str.replace(palavra,letra,'ipi')
    elif letra in 'o':
        palavra = str.replace(palavra,letra,'opo')
    elif letra in 'u':
        palavra = str.replace(palavra,letra,'upu')
       
            
            
    return palavra