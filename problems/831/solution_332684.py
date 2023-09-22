def lingua_p(palavra):
    string_saida=''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
        	string_saida+=letra+'pe'+letra
        else:
            string_saida+=letra
    return string_saida