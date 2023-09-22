def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
    onde cada palavra dessa string é uma chave e tem como
    valor o número de vezes que a palavra aparece"""
    cont_frases= {}
    lista_frase= str.split(frase)
    for palavras in lista_frase:
        freq=list.count(lista_frase)
        cont_frases[palavras]=freq
    return cont_frases
# Escolha nomes elucidativos para suas variáveis