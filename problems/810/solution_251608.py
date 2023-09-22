def retira_pontuacao(a):
    b=a.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ").replace(":"," ").replace("-"," ").replace(";"," ")
    return b

def inverte(c):
	x=str.lower(c)
	list.reverse(x)
    retira_pontuacao(x)
    return x