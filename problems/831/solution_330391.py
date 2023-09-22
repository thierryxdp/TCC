def lingua_p (palavra):
    '''
       Função que recebe uma palavra (palavra) em portugues
       e retorna a mesma palavra traduzida pra o idioma P. 
       Após cada vogal da palavra original, é inserida a 
       sequência de letras 'p' mais a vogal original.
       str -> str
    '''
    palavra=str.lower(palavra)
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in range(len(palavra)):
        if palavra[i] in vogal:
            palavra=palavra.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
            i+=2
    return palavra