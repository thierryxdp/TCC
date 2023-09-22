def retira_pontuacao(frase):
    """funçao que dada uma frase, retira a pontuação e retorna a frase substituindo a pontuação por espaço."""
    """string->string"""
    ponto="-",",",":",";",".","...","!","?"
    str.replace(frase,ponto," ")