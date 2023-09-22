def posLetra(texto,letra,num):
    '''Dados um texto, uma letra e um número (1 para
    primeira ocorrência, 2 para segunda...), retorna a 
    posição da string em que a ocorrência da letra está,
    caso exista menos ocorrências da letra do que a
    ocorrência pedida, a função retornará -1.
    str, str, int -> int'''
    
    if str.count(texto,letra)<num:
        return -1
    else:
        i = 0
        letras = []
        caracteres = list(texto)
        while i < len(caracteres) and len(letras) < num:
            if letra == caracteres[i]:
                list.append(letras,caracteres[i])
            i = i + 1
        return i - 1