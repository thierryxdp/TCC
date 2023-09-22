def conta_frases(frase):
    
    palavra = (frase.split())
    tamanho_palavra = len(palavra)
    contador_palavras = 0
    letra = []
    frases = 0
    while (contador_palavras != tamanho_palavra):
        contador_letras = 0
        palavra_atual = palavra[contador_palavras]
        tamanho_palavra_atual = len(palavra_atual)
        
        if(palavra_atual[-1] == palavra_atual[-2]):
            frases = frases + 1
            contador_palavras = contador_palavras + 1
        else:
            while (contador_letras != tamanho_palavra_atual):
                letra = palavra[contador_palavras][contador_letras]
                contador_letras = contador_letras + 1
                if(letra == "!"):
                    frases = frases + 1
                if(letra == "."):
                    frases = frases + 1
                if(letra == "?"):
                    frases = frases + 1
            contador_palavras = contador_palavras + 1
    print(frases)