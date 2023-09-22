import math
def conta_frases(s):
    """calcula e retorna o número de frases qua aparece num texto 's';str->int"""
    if int(str.count(str(s),'...'))>=1 :
        return int(str.count(str(s),'.'))-2*(int(str.count(str(s),'...')))+int(str.count(str(s),'!'))+int(str.count(str(s),'?')) 
    else:
        return int(str.count(str(s),'!'))+int(str.count(str(s),'.'))+int(str.count(str(s),'?'))+int(str.count(str(s),'...'))