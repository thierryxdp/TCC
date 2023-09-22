def uppCons(frase):
    #"Acumulador para o while"
    contador = 0
    #" Registra todos as consoantes"
    consoantes = ("qwrtypsdfghjklçzxcvbnm")
    #" While determina a rodagem por todos caracteres da frase "
    while contador < len(frase):
        #" Verifica se cada caracteres da frase tem uma cosoantes minuscula "
        if frase[contador] in consoantes:
            # Caso, tenha substitui a cosoante minuscula por maiúscula "
           frase =str.replace(frase,frase[contador],str.upper(frase[contador]))
        contador = contador + 1

    return frase