def lingua_p(palavra):
    palavra2=''
    for letra in palavra:
        if letra not in 'QWRTYPSDFGHJKLMNBVCXZqwrtyplkjhgfdszxcvbnm':
            palavra2= palavra2 + letra +'p'+letra
        else:
            palavra2= palavra2+letra
    return palavra2