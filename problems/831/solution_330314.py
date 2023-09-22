def lingua_p(palavra):
    """Função que recebe uma palavra e retorna ela na língua do P, onde após cada vogal é inserida a sequendia de letras 'p' + a vogal original
	str -> str"""
    
    vogais = "aeiouáàâãéèêíìîóòôõúùû"
    linguap = ""
    
    for letra in palavra:
        if letra in vogais:
            linguap = linguap + letra + 'p' + letra
        
        else:
            linguap = linguap + letra
    
    return linguap