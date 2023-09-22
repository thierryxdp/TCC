def uppCons (frase):
    '''funcao que dada um frase,retornará a frase com todas as suas consoantes em maiculas,os caracteres voltarão para fraseoriginal
    str-> str'''
    frase1 =''
    tamanho = 0 
    consoante = 'bcdfghjklmnnpqrstvwxyzç'
    while tamanho < len(frase1):
        if frase1[tamanho] in consoante:
            frase1 = frase1 + (str.upper(frase[tamanho]))
        else:
            frase1 = frase1 + frase[tamanho]
        tamanho = tamanho + 1
        return frase21