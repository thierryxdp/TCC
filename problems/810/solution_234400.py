def inverter(texto):
    
#remove  a pontuação de uma frase, transforma as letras em minusculas e inverte sua ordem 

    f = str(texto)
    f = str.lower(texto)

    f = f.replace("!", "")
    f = f.replace("...", "")
    f = f.replace("?", "")
    f = f.replace(",", "")
    f = f.split()

    x = f[-1::-1]

    return ' '.join(x)