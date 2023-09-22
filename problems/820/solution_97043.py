def posLetra(string,letra,num):
    ocorrencia = num
    qtd_letras = ()
    while letra in string:
        qtd_letras = qtd_letras + 1
    return qtd_letras