def lingua_p(palavra:str) -> str:
    """Traduz uma palavara para a língua do p, isto é, vogal + p + vogal anterior ao longo da palavra

       Parameters:
       palavra: palavra em português

       Returns:
       Palavra na língua do p. Ex: então -> epentãpãopo
    """
    str.lower(palavra)
    palavra_p = list(palavra)
    qtd_silaba = 0 
    for letra in range(len(palavra)):
        if palavra[letra] in 'aeiouãõáéíóúêôà':
            silaba = 'p' + palavra[letra]
            list.insert(palavra_p,letra + 1 +qtd_silaba,silaba)
            qtd_silaba += 1
        
    return str.join('',palavra_p)