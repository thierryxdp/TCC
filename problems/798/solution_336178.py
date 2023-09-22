def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário
       onde cada palavra dessa string seja uma chave e tenha
       como valor o número de vezes que a palavra aparece.
       : param frases: str
       : return: dict
    '''
    quantas_vezes={}
    separado=frases.split()
    for palavra in separado:
        quantas_vezes.update({palavra:separado.count(palavra)})
    return quantas_vezes