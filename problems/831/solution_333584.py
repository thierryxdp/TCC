From operator import contains
def lingua_p(palavra):
    if contains(palavra,'a'):
        palavra=palavra.replace('a','apa')
    return palavra