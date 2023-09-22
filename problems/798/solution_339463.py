"""Dada uma string, retorna as palavras o número de vezes que elas são repetidas"""
#str-->dic
def freq_palavras(st):
    st2=st.split()
    freq={}
    for x in st2:
        if (x in freq):
            freq[x]+=1
        else: 
            freq[x]=1
	return freq