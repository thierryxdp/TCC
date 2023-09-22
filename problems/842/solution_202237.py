#Start your python function here
def P1(a, b, c, d):
    p1 = 0
    if a > b:
        p1 += 3
    if d > c:
        p1 += 1
    return p1
def P2(a, b, c, d):
    p2 = 0
    if a < b:
        p2 += 3
    if c > d:
        p2 += 1
    return p2

def pontos_por_time(ida_volta):
    return {ida_volta[0][0] : P1(ida_volta[0][2][0], ida_volta[0][2][1],ida_volta[1][2][0],ida_volta[1][2][1]),
    ida_volta[0][1] : P2(ida_volta[0][2][0],ida_volta[0][2][1],ida_volta[1][2][0],ida_volta[1][2][1])
    }