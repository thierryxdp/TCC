def conta_frases(numFrases):
    """ funcao que conta o numero de frases que aparece no texto"""

a = str.join('.', str.split(numFrases, '...'))
c = str.join('.', str.split(a, '?'))
d = str.join('.', str.split(c, '!'))
sulucao=str.count(d,".")
    return solucao