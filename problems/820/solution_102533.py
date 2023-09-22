def posLetras (frase,letra,n):
    a = str.find(frase, letra)
    ocorrencia = 1
    while ocorrencia < n:
        x = str.find(frase,letra, a+1)
        a = x + 1
        ocorrencia = ocorrencia + 1