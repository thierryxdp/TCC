def lingua_p(palavra):
    
    resposta=''
    
    for vogal in palavra:
        if vogal in 'aeiou':
            vogal = vogal + 'p' + vogal
        resposta+=1
    return str.lower(respota)