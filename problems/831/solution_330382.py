def lingua_p (palavra):
    '''
       Função que recebe uma palavra (palavra) em portugues
       e retorna a mesma palavra traduzida pra o idioma P. 
       Após cada vogal da palavra original, é inserida a 
       sequência de letras 'p' mais a vogal original.
       str -> str
    '''
    palavra=str.lower(palavra)
    i=0
    while i<len(palavra):
        vogal='aeiouáéíóúãõãêîôûàèìòù'
        if palavra[i] in vogal:
            sub=palabre[i]+'p'+palavra[i]
            palavra = palavra.replace(palavra[i],sub)
        i=i+1
    return palavra