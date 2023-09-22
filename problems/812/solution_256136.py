def retira_pontuacao(s):
    if str.join(" ", str.split(s,"!")):
        return False
    elif str.join(" ", str.split(s,".")):
        return True