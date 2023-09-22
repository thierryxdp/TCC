'''Esta função nos retorna a quantidade de frases dentro de um certo pedaçõ de texto'''
'''Para isso o procedimento realiza a contagem de aparecimentos dos caracteres que determinam
o término de uma frase, que são eles: '.' , '!' , '?' , '...' '''
def conta_frases(periodo):
    a = periodo.count('.')
    b = periodo.count('!')
    c = periodo.count('?')
    frases = a+b+c
    if a >= 3:
        retic = periodo.count('...')
        if retic == 0:
            a = 3
        elif retic > 0:
            a = retic + a
    return frases