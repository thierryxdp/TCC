# recebe uma string e coloca o # no inicio no meio e no fim
# str-> str
def hashtag(s):
    meio = (len(s)//2) 
    fim = len(s)
    return '#' + s[:meio] +'#'+ s[meio:fim]+'#'