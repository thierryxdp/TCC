def lingua_p(palavra):
    ''' recebe uma palavra e retorna a mesma palavra mas com o acrescimo da letra p após cada vogal'''
    vogais = 'aeiou'
    for letra in palavra:
        if letra in vogais:
            return palavra+'p'