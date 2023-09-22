# a função retira pontuação , pois queremos contabilizar apenas as palavras
# Escolha nomes elucidativos para suas variáveis
# string -> int

    
    def semPontuacao(A):
    pontuacao = ".,:?!; "

    for x in pontuacao:
        A = A.replace(x, " ")

    return A

	
    def quant_palavras(frase):
        frase = semPontuacao(frase)
    
    H = frase.split()
    	return len(H)