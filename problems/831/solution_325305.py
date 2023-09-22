def lingua_p(string):
    vogais = 'aeiouãõéíáàôâ'
    resposta=''
    for i in string:
        if i in vogais:
            resposta += i + 'p' + i
        else:
            resposta+=i
    return resposta