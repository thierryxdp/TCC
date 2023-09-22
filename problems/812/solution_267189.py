#dado umafrase retorna a mesma sem pontos e com espaço entre elas
#str-->str
def retira_pontuacao(a):
    	import string
        z=string.punctuation
        for x in z:
            a=a.replace(x," ")
        return(a)