def lingua_p(palavra):
    ''' funcao que recebe como parametro uma palavra(em portugues)
     e retorne esta mesma palavra traduzida para a lingua
     do P, a funcao nao distingue letras maiuscula e minuscula
     retornando sempre a palavra traduzida em letras minusculas
     string->string'''
    indice = 0
    frase_tratada=''
    for i in palavra:
        if i not in 'qrtypsdfghjklçzxcvbnm':
            frase_tratada= frase_tratada+ i+ 'p'+ i
        else:
            frase_tratada= frase_tratada +i
    return frase_tratada