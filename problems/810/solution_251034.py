def inverte(frase):
    """Função que, dada uma frase, sejam retiradas a pontuação e letra maiúscula, além de invertê-la; str=>str"""
	p1 = (retira_pontuacao(frase))
	p2 = str.lower(p1)
	p3 = str.split(p2)
	p4 = str.reverse(p3)
	return str.join(" ", lista)