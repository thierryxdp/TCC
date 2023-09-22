def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""

    f1 = frase.split('.'):
        return '  '.join(f1)
    f2 = f1.split('!'):
        return '  '.join(f2)
	f3 = f2.split(','):
        return '  '.join(f3)
    f4 = f3.split('?'):
        return '  '.join(f4)
	f5 = f4.split('...'):
        return '  '.join(f5)
    f6 = f5.split('-'):
    return '  '.join(f6)