def lingua_p(palavra: str) -> str:
    vogais = 'abcde'
    palavra1 = ''
    
    for i in palavra:
        if i in 'aeiou':
            palavra1 += i + 'p'
        else:
            palavra1 += i
            
    return palavra1