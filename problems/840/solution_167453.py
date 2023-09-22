def bolos(a, b, c):
    acc = 0
    while True:
        a -= 2
        b -= 3
        c -= 5
    	if a < 0 or b < 0 or c < 0:
            break
        acc += 1
 
    return acc