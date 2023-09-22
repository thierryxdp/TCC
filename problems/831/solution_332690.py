def lingua_p(palavra):
    string_saida=''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéíóú':
        	string_saida+=letra+'p'+letra
        else:
            string_saida+=letra
    return string_saida