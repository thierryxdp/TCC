def retira_pontuacao(frase):
    """ função que, dada uma frase, retira toda a pontuação dela, substituindo por espaço"""
    x="-"
    y=","
    z=":"
    w=";"
    r="."
    s="!"
    a="?"
    return str.replace(frase,(x,y,z,w,r,s,a), " ")