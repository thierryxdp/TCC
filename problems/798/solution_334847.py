def freq_palavras(frases):
    """A Função recebe uma string e retorna um dicionário onde
	cada palavra dessa string seja uma chave e tenha como valor
	o número de vezes que a palavra aparece;
    str -> dict"""
    lista = str.split(frases)
	dic = {}
    for n in lista:
        qtd = list.count(lista, n)
        if n not in dic:
            dic[n] = qtd
    return dic