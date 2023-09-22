def retira_pontuacao(s):
    if str.join(" ", str.split(s,"!")):
        return str.join(" ", str.split(s,"!"))
    else str.join(" ", str.split(s,".")):
        return str.join(" ", str.split(s,"."))