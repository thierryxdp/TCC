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
        p=i
        if palavra[i] in vogal:
            if str.count(palavra,palavra[i])==1:
                nova=nova.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
            else:
                if palavra.index(palavra[i],i-1,-1)==nova.index(palavra[i],i,-1):
                    nova=nova.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
                else:
                    nova=nova.replace(palavra[i+2],(palavra[i+2]+'p'+palavra[i+2]))
    return nova