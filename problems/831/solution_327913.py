def lingua_p(palavra:str)-> str:
    """Função que, dada uma palavra em português,
    retorna a mesma palavra na língua do P, ou seja,
    após cada vogal da palavra é inserido o p e repetida
    a vogal original."""
    
    palavra_p = list()
    
    for letra in palavra:
        if str.lower(letra) in ("aâãáàeéêiìíoóôõuú"):
            list.append(palavra_p, letra + "p" + letra)
        
        else:
            list.append(palavra_p, letra)
    
    return str.lower(str.join("", palavra_p))