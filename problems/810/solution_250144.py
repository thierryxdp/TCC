def inverte(frase):
    ' str - str '
    ' Função que dada uma frase em string, retorna a frase de trás para frente.'
    frase_nova = str.split(substituicao(frase))
    list.reverse(frase_nova)
    f = " ".join(frase_nova)
    return f