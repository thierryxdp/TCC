def uppCons (frase):
    '''funcao que dada um frase,retornará a frase com todas as suas consoantes em maiculas,os caracteres voltarão para fraseoriginal
    str-> str'''
    frase21 =''
    tamanho = 0 
    consoante = 'bcdfghjklmnnpqrstvwxyz'
    while tamamho < len(frase21):
        if frase21[tamanho]in consoante:
            frase21 =frase21 + (str.upper(frase[tamanho]))
            else:
                frase21 = frase21 + frase[tamanho]
                tamanho =tamanho + 1
                return frase21