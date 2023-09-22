"""Dado um número, calcula e retorna o fatorial do mesmo:
int->int"""
def fatorial(k):
    i=1
    kfat=1
    while i<=k:
        kfat=kfat*i
        i=i+1
    return kfat