def lingua_p(palavra):
    
    '''recebe uma uma palavra e retorna a mesma palavra na lingua
       do p, desprezando as letras maiusculas e minusculas 
       retornando tudo em minuscula
       str->str'''
    vogal=""
    for indice in range(len(palavra)):
        if palavra[indice] in "aeiouAEIOU":
            vogal=vogal+palavra[indice]+"p"+palavra[indice]
        else:
            vogal=vogal+palavra[indice]
    return str.lower(vogal)
lingua_p("matheus")