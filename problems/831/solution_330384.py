def lingua_p (palavra):
    '''
       Função que recebe uma palavra (palavra) em portugues
       e retorna a mesma palavra traduzida pra o idioma P. 
       Após cada vogal da palavra original, é inserida a 
       sequência de letras 'p' mais a vogal original.
       str -> str
    '''
    palavra=str.lower(palavra)
    for letra in palavra:
        vogal='aeiouáéíóúãõãêîôûàèìòù'
        if letra in vogal:
            palavra.replace(letra,(letra+'p'+letra))
        return palavra