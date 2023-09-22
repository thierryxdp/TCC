def lingua_p(palavra_port):
    '''Função que recebe uma palavra em português e a retorna
    traduzida para a língua do P.Uma palavra foi traduzida para
    a língua do P quando,ap ́os cada vogal da palavra original,é
    inserida a sequência de letras p mais a vogal original. A
    resposta deve vir em minúsculos. str->str'''
    minusculo=palavra_port.lower
    resposta = ''
    for i in minusculo:
        if i in 'aeiouáéíóúâêôãõ':
            i = i + 'p' + i
            resposta = resposta + i
        else:
            resposta = resposta + i
    return resposta