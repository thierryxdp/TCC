def lingua_p(palavra):
    """retorna a palavra traduzida para a lingua do P
    (após cada vogal é inserida o 'p' mais a vogal original)"""
    
    linguaP = ''
    
    for letra in palavra:
        if letra in "AEIOUaeiouáéíóú":
            linguaP = linguaP + (letra) + ('p') + (letra)
        else:
            linguaP = linguaP + (letra)
            
    return str.lower(linguaP)