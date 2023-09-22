def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """
    
    
    
    
    for letra in palavra:
        if letra in 'a':
            palavra = str.replace(palavra,letra,'pap')
        elif letra in 'e':
            palavra = str.replace(palavra,letra,'pep')
        elif letra in 'i':
            palavra = str.replace(palavra,letra,'pip')
        elif letra in 'o':
            palavra = str.replace(palavra,letra,'pop')
        elif letra in 'u':
            palavra = str.replace(palavra,letra,'pup')
        
            
            
    return palavra