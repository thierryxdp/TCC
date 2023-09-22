import re
def retira_pontuação(frase,pontuação)
"""função que retira a pontuação do texto
entrada: str
texto= -duda,foi;a:praia.
str(pontuação"-"","":"";""."
saida: str""""
return re.compile(f'({"|".join(map(re.escape, retira_pontuação))})') texto= r.sub('',texto)