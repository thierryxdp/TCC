def retira_pontuacao(rp):
    str.replace(rp,"-"," ")
    str.replace(rp,"!"," ")
    str.replace(rp,";"," ")
    str.replace(rp,":"," ")
    str.replace(rp,","," ")
    str.replace(rp,"?"," ")
    str.replace(rp,"."," ")
    return 
def inverte(iv):
    r = retirapontuacao(iv)
    iv.split = r
    list.reverse(iv)
    return iv