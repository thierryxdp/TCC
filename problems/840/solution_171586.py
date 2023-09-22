from math import floor

def bolos(a,b,c):
    return floor(min(a/2,b/3,c/5))

print(bolos(2,40,6))