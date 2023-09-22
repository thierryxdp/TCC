# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
       onde cada palavra dessa string seja uma chave e tenha
       como valor o número de vezes que a palavra aparece;
       string -> dict"""
    palavra = ''
    dicionario = {}
    for letra in frases:
        if letra != ' ':
            palavra = palavra + letra
            numero_vezes = str.count(frases,palavra)
        elif len(palavra) < 3 and palavra != frases[0]:
            palavra = ' ' + palavra + ' '
            numero_vezes = str.count(frases,palavra)
            palavra = str.replace(palavra,' ','')
        if (letra == ' ' or letra == frases[-1]) and palavra != '':
            if (palavra + '.' in frases) or (palavra + 's' in frases and len(palavra)>2):
                numero_vezes = numero_vezes - 1
                dicionario[palavra] = numero_vezes
                palavra = ''
            else:
                dicionario[palavra] = numero_vezes
                palavra = ''
        
    return dicionario