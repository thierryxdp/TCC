def lingua_p(palavra):
    """Função que retorna a palavra de entrada traduzida para a língua do P, onde após cada vogal, é inserida a sequência de letras 'p' mais a vogal original
str -> str"""

    palavra_final = ''
    
    for caractere in palavra:
        if caractere in 'aeiouáéíóú':
            caractere = caractere + 'p' + caractere
        palavra_final = palavra_final + caractere
    return str.lower(palavra_final)