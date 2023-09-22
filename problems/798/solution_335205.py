freq_palavras(frases):
    """Recebe uma string e retorna um dicionário no qual cada palavra
    dessa string seja uma chave e tenha como valor o número de vezes
    que a palavra aparece;
    str -> dict"""
    pontuacoes = ".,:;_?!"
    for caractere in frases:
        if caractere in pontuacoes:
            nova_frase = frases.replace(caractere, "")
    palavras = nova_frase.split()
    freq = {}
    for palavra in palavras:
        if palavra not in freq:
            freq[palavra] = 1
        else:
            freq[palavra] = freq.get(palavra) + 1
    return freq