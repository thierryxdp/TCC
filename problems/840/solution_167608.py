def bolos(a, b, c):
    x = a/2
    y = b/3
    z = c/5
    if a >= 2:
        if b >= 3:
            if c >= 5:
                return (a + b + c)//10
            if x < 1:
                if y < 1:
                    if z < 1:
                        return 0
                    if c < 5:
                        return 0