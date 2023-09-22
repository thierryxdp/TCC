def freq_palavras(frases):
    "funçao que recebe uma string e retorna um dicionario onde cada palavra dessa string seja uma chave e tenha como valor o numero de vezes que a palavra aparece"
    freq={}
    ocorrencias=0
    separados=frases.split(' ')
    for i in range(len(separados)):
        ocorrencias=separados.count(separados[i])
        freq[separados[i]]=ocorrencias
    return freq