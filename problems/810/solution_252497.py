def retira_pontuacao(frase):
    """função que recebe string com caracteres e retorna outra string substituindo-os por espaço. string string"""
    frase=frase.replace("–", " ").replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")
    return frase

def inverte(frase):
    'função que inverte a ordem de uma frase. Será retirada a pontuação e trocadas maiúsculas por minúsculas . string string'
    novafrase=(str.split(str.lower(retira_pontuacao(frase))))
    invertida=str.join(" ",(novafrase[(len(novafrase)):0:-1]))
    return invertida