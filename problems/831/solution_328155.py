def lingua_p(palavra: str) -> str:
    vogais = 'abcde'
    palavra1 = ''
    
    for i in palavra:
        if i in 'abcde':
            palavra1 += 'p' + i
        else:
            palavra1 += i
    return palavra1