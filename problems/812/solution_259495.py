import re
def retira_pontuacao(x):
    frasenova = x
    return (re.sub('... - . / ? ! @ # $ % ¨,:;',' 'x))