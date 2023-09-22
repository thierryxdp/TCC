"""Retorna a frase onde todos os caracteres de pontuação são substituidos por espaço:
str->str"""
def retira_pontuacao(y):
    if '!' or '.' or '?' or '...':
        return ' '