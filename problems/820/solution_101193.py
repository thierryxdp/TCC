def posletra(stri,let,num):
    '''função que retorna a posição na string em que a ocorrencia desejada,num, de letra,let, se encontra na frase,frase,retornando menos 1 caso não haja ocoorência da letra'''
     if stri.count(let) < num:
        return -1
    else:
        i = 0
        letras = []
        caracteres = list(stri)
        while i < len(caracteres) and len(letras) < num:
            if let == caracteres[i]:
                list.append(let, caracteres[i])
            i = i + 1
        return i - 1