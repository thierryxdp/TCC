"""Dada uma string "s", retorna o caractere"#" no início,
meio e fim dela
str-> str"""
def hashtag(s):
    meio = len(s)//2
    return "#" + s[:meio] + "#" + s[meio:] + "#"