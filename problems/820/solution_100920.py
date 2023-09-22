def posLetra(frase,letra,ocorrencia):
    "Função que dado uma frase, uma letra e o númera que corresponde a ocorrencia da letra, retorna em qual posição está a letra na ocorrencia. str, str, int --> int"
    i = 0
    ocs = 0
    while i<len(frase) and ocs!=ocorrencia:
        if frase[i] == letra:
            ocs = ocs +1
        i = i + 1
    if ocs == ocorrencia:
        return i-1
    else:
        return -1