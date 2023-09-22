def lingua_p(palavra):
    """
    Essa função, dado uma palavra em formato de string como argumento,
    ira retornar essa mesma palavra traduzida para a lingua do p
    onde cada vogal ira ser sucedida e antecedida pela letra p
    str->str
    """
    
    
    nova_palavra=''
    
    for letra in palavra:
        if letra in 'a':
            nova_palavra = str.replace(palavra, letra, 'pap')
        elif letra in 'e':
            nova_palavra = str.replace(palavra,letra,'pep')
        elif letra in 'i':
            nova_palavra = str.replace(palavra,letra,'pip')
        elif letra in 'o':
            nova_palavra = str.replace(palavra,letra,'pop')
        elif letra in 'u':
            nova_palavra = str.replace(palavra,letra,'pup')
        else:
            nova_palavra += letra
            
            
    return nova_palavra