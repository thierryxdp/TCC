def lingua_p(palavra):
    '''Função que recebe uma palavra(em portugues) e retorne
       esta mesma palavra traduzida para a lingua do P. No
       qual após cada vogal da palavra original, é inserida
       a sequencia de letras 'p' + vogal original. 
       : param palavra: str
       : return: str
    '''
    traduzido=''
    vogal='aeiouéáú'
    for letra in palavra:
        if letra in vogal:
            traduzido=traduzido+letra+'p'+letra
        if letra not in vogal:
            traduzido=traduzido+letra
    return traduzido