def posLetra(frase, letra, num):
    '''função responsável por retornar a posição do termo,letra, na ocorência desejada,num,na frase desejada,frase'''
    if frase.count(letra) < num:
        return -1
    else:
        i = 0
        letras = []
        caracteres = list(frase)
        while i < len(caracteres) and len(letras) < num:
            if letra == caracteres[i]:
                list.append(letras, caracteres[i])
            i = i + 1
        return i - 1