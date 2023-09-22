def inverte(frase):
    """função que, dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúscula, e sem a pontuação."""
    frase=str.split(retira_pontuacao(frase), " ")
    frase=str.join(" ",frasepica[::-1])
    return str.replace(str.lstrip(frase.lower()),"  "," ")