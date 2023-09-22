def retira_pontuacao(frase):
    """
    Faca uma funcao que dada uma frase, substitua todos os caracteres especiais por um espaço(" ").
    frase: string.
    return: string.
    """
#Traveção 
    frase = str.split(frase, '-')
    frase = str.join(" ", frase)
#Virgula
    frase = str.split(frase, ',')
    frase = str.join(" ", frase)
#dois pontos    
    frase = str.split(frase, ':')
    frase = str.join(" ", frase)
#Ponto e virgula
    frase = str.split(frase, ';')
    frase = str.join(" ", frase)
#Exclamação
    frase = str.split(frase, '!')
    frase = str.join(" ", frase)
#Interrogação
    frase = str.split(frase, '?')
    frase = str.join(" ", frase)
#Ponto final
    frase = str.split(frase, '.')
    frase = str.join(" ", frase)
    return frase