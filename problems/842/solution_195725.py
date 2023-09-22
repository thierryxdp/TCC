a = ['t1','t2',[g1,g2]]
b = ['t2','t1',[g3,g4]]
g1 = 1
def pontos_por_time(a,b):
    if g1>g2:
        return g1 == 3
    if g2>g1:
        return g2 == 3
    if g1==g2:
        return g1 == 1 and g2 == 1
    if g3>g4:
        return g3 == 3
    if g4>g3:
        return g4 == 3
    if g3==g4:
        return g3 == 1 and g4 == 1
        return {a,b}