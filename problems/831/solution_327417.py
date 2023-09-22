def lingua_p(palavra):
    palavra = list(palavra)
    mensagem = ''
    i = 0
    while i <= len(palavra):
        if palavra[i] in 'aeiou':
            palavra[i] += 'p' + palavra[i]
            mensagem += palavra[i]
        else:
            
            mensagem += palavra[i]
        i += 1
    return mensagem