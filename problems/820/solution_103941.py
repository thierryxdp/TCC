def posLetra(texto, letra, numero):
    if(texto.count(letra) > numero):
        return -1
    helper = 0
    
    for i, letra in enumerate(texto):
        print(letra, i)