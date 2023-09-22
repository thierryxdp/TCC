def freq_palavras(frase):
    """Função que pega cada palvra da frase, conta quantas vezes ela aparece, criando um dicionário onde a palvra é a chave e as aparições o valor"""
    """Parâmetros de entrada:str"""
    """Parâmetros de saída:dic"""
    vazio={}
    lista_de_palavras=frase.split(' ')
    for elemento in lista_de_palvras:
        vazio[elemento]=lista_de_palavras.count(elemento)
    return vazio