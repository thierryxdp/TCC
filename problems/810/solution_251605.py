def retira_pontuacao(a):
    b=a.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ").replace(":"," ").replace("-"," ").replace(";"," ")
    return b

def inverte(b):
	x=str.lower(b)
	list.reverse(x)
    retira_pontuacao(x)
    return x