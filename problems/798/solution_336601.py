def freq_palavras(frases):
	'''funçao que recebe um frase eretorna um dicionario com o numero de vezes que cada palavra repete;
    str->float'''# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

	dicpalavras=[]
    frase = str.split(frases)
    
    for palavras in frase:
        dicpalavras[palavras]= 1
    return dicpalavras