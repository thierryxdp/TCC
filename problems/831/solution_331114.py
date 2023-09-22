def lingua_p(palavra):
    '''
Função que receba como parametro uma palavra (em português) 
e retorna esta mesma palavra traduzida para a língua do P.
Logo após cada vogal da palavra original, ser inserida a
sequencia de letras p mais a vogal original.
    str-->str
    '''
    frase=''
    vogais='aeiouAEIOUáéíú'
    palavra.lower()
    for i in palavra:
        if i in vogais:
            frase=frase+i+'p'+i
        else:
            frase=frase+i
            
    return frase