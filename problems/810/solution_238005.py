def inverte(frase):
    """função que, dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúscula, e sem a pontuação."""
    frasepica=str.split(retira_pontuacao(frase), " ")
    frasepica=str.join(" ",frasepica[::-1])
    return str.replace(str.lstrip(frasepica.lower()),"  "," ")