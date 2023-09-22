''' função que recebe uma string e insere a "#" no inicio, no meio e
   no fim'''
''' str-> str'''
def hashtag(s):
    meio= len(s)//2
    return "#" + s[:meio]+ "#" + s[meio:] + "#"