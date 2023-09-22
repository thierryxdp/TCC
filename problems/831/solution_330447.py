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
    p=0
    for i in range(len(palavra)):
        if palavra[i] in vogal:
            if str.count(palavra,palavra[i])==1:
                nova=nova.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
            else:
                nova=nova.replace(nova[i+2],(palavra[i]+'p'+palavra[i+2]))
                p=i+1
    return nova