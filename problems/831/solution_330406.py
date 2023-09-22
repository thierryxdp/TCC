def lingua_p (palavra):
    '''
       Função que recebe uma palavra (palavra) em portugues
       e retorna a mesma palavra traduzida pra o idioma P. 
       Após cada vogal da palavra original, é inserida a 
       sequência de letras 'p' mais a vogal original.
       str -> str
    '''
    palavra=str.lower(palavra)
    nova=palavra
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in range(len(palavra)):
        p=i
        if palavra[i] in vogal:
            nova=nova.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
            p=i+2            
    return nova