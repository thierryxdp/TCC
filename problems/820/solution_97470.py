def posLetra(frase, letra, numero):
        """função que dada uma string, uma letra e um número que indica uma ocorrencia, retorne em qual posição da string a ocorrencia da letra esta;str,str,int-->int"""
        in frase.count(letra)<numero:
            return -1
        a=0
        b=0
        while b!=numero:
            if letra==frase[a]:
                posOcorrencia=a
                b+=1
            a+=1
        return posOcorrencia