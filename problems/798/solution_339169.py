def freq_palavras(frases):
    '''Retorna um dicionário onde cada palavra da string inserida é uma
    chave e o número de vezes que ela aparece o valor correspondente;
    str -> dict'''
    dicionario={}
    for i in range(len(frases)):
        if frases[i]=' ':
            Palavra=frases[0:i]
            valor=frases.count(Palavra)
            dicionario[Palavra]=valor
            frases.replace(frases[0:i+1],'')
	return dicionario