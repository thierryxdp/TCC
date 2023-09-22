import re

def retira_pontuacao(string):
    return(re.sub("[-,:;.!?]"," ", string))