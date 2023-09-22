def lingua_p(palavra):
    '''Função que pega a palavra de entrada e retorna a tradução para língua P 
        str,str→str'''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            letra_nova= letra +'p' + letra
            contagem_letra= palavra.count(letra)
            if contagem_letra > 3:
               palavra= palavra
            else:
                palavra=palavra.replace(letra,letra_nova,contagem_letra)
    return palavra