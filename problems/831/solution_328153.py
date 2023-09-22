def lingua_p(palavra: str) -> str:
    vogais = 'abcde'
    palavra1 = ''
    
    for i in palavra:
        if i in 'abcde':
            palavra1 += i + 'p'
            
    return palavra1