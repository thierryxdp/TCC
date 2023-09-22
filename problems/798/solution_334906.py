def freq_palavras(frases):
    """Dada uma string, a função vai retornar um dicionario onde
    cada palavra da string é um chave e seu conteúdo é a quantidade
    de vezes que a palavra aparece na string.
       A frase deve ser colocada entre aspas;
       str --> dic"""
    frases = frases.split()
    dicionario = {}
    for palavra in frases:
        qunt_aparece = list.count(frases,palavra)
        dicionario.update({palavra:qunt_aparece})
    return dicionario