""" Retorna o caractere "#" no início, no meio e no fim de uma palavra
Recebe a palavra (s)
str-> str"""
import math
def hashtag(s):
    return "#" + part1(s) + "#" + part2(s) + "#"             
def met1 (s):
    return math.floor (comp(s)/2)
def met2 (s):
    return math.floor(comp(s)/2) + 1
def comp (s):
    return len (s)
def part1(s):
    return s[0: met1(s)]
def part2(s):
    return s[met1(s):]