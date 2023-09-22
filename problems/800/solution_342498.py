# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(l,d):
    a = []
    for e in l:
        a.append(d[e])
    return round(sum(a),2)