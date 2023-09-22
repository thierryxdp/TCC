'''Esta função nos retorna a quantidade de frases dentro de um certo pedaçõ de texto'''
'''Para isso o procedimento realiza a contagem de aparecimentos dos caracteres que determinam
o término de uma frase, que são eles: '.' , '!' , '?' , '...' '''
def conta_frases(periodo):
    a = periodo.count('.')
    b = periodo.count('!')
    c = periodo.count('?')
    if '...' in periodo:
        d = periodo.count('...')
        return a+b+c+d
    else:
        return a+b+c