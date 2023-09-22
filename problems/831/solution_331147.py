def lingua_p(palavra):
    '''Traduz a palavra de entrada na língua do pê. Se a palavra estiver com alguma letra maiúscula,
tornar-se-á minúscula.
str --> str
'''
    palavra_tratada = str.lower(palavra)
    nova = ''
    for letra in palavra_tratada:
        if letra in 'aâãáeéêiíoôõuú':
            nova += letra+ 'p'+ letra
        else:
            nova += letra
    return nova