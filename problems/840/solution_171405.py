def bolos(xt,no,cl):
    from math import floor
    return min(floor(xt-2),floor(no-3),floor(cl-5))