def lingua_p (palavra):
    """Função que, dada uma palavra, retorna a mesma palavra traduzida para a língua do P, na qual, após cada vogal da letra original, insere 'p' mais a vogal original.
    entrada: str
    saída: str"""
    
    palavra_min = str.lower(palavra)
    palavra_nova = ''
    
    for letra in palavra_min:
        if letra in 'aeiou':
            palavra_nova = palavra_nova + letra + 'p' + letra
            
        if letra not in 'aeiou':
            palavra_nova = palavra_nova + letra
            
    return palavra_nova