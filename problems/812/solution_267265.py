def retira_pontuacao(rp):
    """Recebe uma string e substitui por uma string alterada str-->str"""
    rp=str.replace(rp,"-"," ")
    rp=str.replace(rp,"!"," ")
    rp=str.replace(rp,";"," ")
    rp=str.replace(rp,":"," ")
    rp=str.replace(rp,","," ")
    rp=str.replace(rp,"?"," ")
    rp=str.replace(rp,"."," ")
    return rp