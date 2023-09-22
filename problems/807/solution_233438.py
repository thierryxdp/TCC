'''Esta função nos retorna a quantidade de frases dentro de um certo pedaçõ de texto'''
'''Para isso o procedimento realiza a contagem de aparecimentos dos caracteres que determinam
o término de uma frase, que são eles: '.' , '!' , '?' , '...' '''
def conta_frases(periodo):
    a = periodo.count(''.'')
    b = periodo.count('!')
    c = periodo.count('?')
    d = periodo.count('...')
    frases = a+b+c+d
    return frases