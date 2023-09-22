def num_bombons(x,y):
    bombons=0
    custo=0
    while custo + y < x:
        bombons += 1
        custo += y
    return bombons