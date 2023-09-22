def retira_pontuacao(frase, caractere):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    if str.count(frase,caractere) == 0:
        return "Caractere não encontrado"