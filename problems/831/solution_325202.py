def lingua_p(palavra):
    
    resposta=''
    
    for vogal in palavra:
        if vogal in 'aeiou':
            vogal = vogal + 'p' + vogal
        resposta = resposta + vogal
    return str.lower(respota)