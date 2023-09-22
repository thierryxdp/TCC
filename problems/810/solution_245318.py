def inverte(frase):
    '''
    funçao que reecebe uma frase e retorna uma outra que contenha as mesmas palavras da frase de entrada na ordem inversa, sem laiusculas e pontuação;
    str -> str
    '''
    frase1 = str.replace(frase,'.','')
    frase2 = str.replace(frase1,'!','')
    frase3 = str.replace(frase2,'?','')
    frase4 = str.replace(frase3,'...','')
    frase5 = str.replace(frase4,',','')
    frase6 = str.replace(frase5,'-',' ')
    frase7 = str.replace(frase6,':','')
    frase8 = str.replace(frase7,';','')
    minusculos = frase8.lower()
    frase_final = str.split(minusculos)
    list.reverse(frase_final)
    resultado = str.join(' ',frase_final)
    return resultado