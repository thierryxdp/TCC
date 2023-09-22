# Essa função inseri o carcater '#' no ínicio, meio e no final
# da nossa string 's'
# str-> str
def hashtag(s):
    return str('#')+s[0:int(len(s)/2)]+str('#')+ s[int(len(s)/2):len(s)]+str('#')