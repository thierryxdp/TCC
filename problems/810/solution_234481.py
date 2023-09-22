def inverte(frase):
    """Dada uma frase a função retorna outra frase que contém as mesmas palavras da frase
    de entrada na ordem inversa, sem letras maiúsculas e sem a pontuação;
    str --> str"""
    minusculas = str.lower(frase)
    retPontuacao = retira_pontuacao(minusculas)
    separaPalavras = str.split(retPontuacao)
    novaFrase = str.join(' ', separaPalavras[-1::-1])
    return novaFrase