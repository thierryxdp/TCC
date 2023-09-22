def uppCons(frase):
    """Esta é a função que dada uma frase, retorna a frase com suas consoantes maiúsculas; str -> str"""
    i = 0

    while i < len(frase):
        letra = frase[i]
        
        if letra in "AEIOUaeiou":
            i = i + 1

        else:
            i = i + 1
            frase = str.replace(frase,letra,letra.upper())
            
    return frase