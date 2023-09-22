import re
def conta_frases(frase):
    return (re.split('! | ? |...|.', frase))