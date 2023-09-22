def retira_pontuacao (frase):
    """Função que substitui todos os caracteres de pontuação por espaço, dada uma frase
    entrada: str
    saída: str"""
    
    for caracter in ".,:;?!":
        texto = frase.replace(caracter, ' ')
        return texto