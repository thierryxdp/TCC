from math import *
def mdc1(A,B):
    """maior divisor comum entre A e B"""
    return gcd(A//2,B//3)
def mdc2(B,C):
    """maior divisor comum entre B e C"""
    return gdc(B//3,C//5)
def mdc3(A,C):
    """maior divisor comum entre A e C"""
    return gdc(A//2,C//5)
from math import *
def xxxxx(A,B,C):
    """yyyyyyyyyyy""" 
    return (mdc3(A,C)+ mdc2(B,C) + mdc1(A,B))/3