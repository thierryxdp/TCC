def retira_pontuacao(frase):
    """recebe uma frase e retorna outra sem as pontuações 
    	da primeira
        str -> str"""
    s = frase
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(s,"-"," "),";"," "), "/", " "),":", " "),"|"," "),","," "),"..."," "),"?"," "),".", " "),"!"," ")

def inverte(s):
    """Recebe uma string e retorna esta sem pontuação e invertida
    str -> str"""
    s = retira_pontuacao(s)
    return str.join(" ", s.split()[-1::-1])