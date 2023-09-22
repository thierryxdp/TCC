""" Essa função (freq_palavras) pega uma string com um texto e devolve
   um dicionário que relaciona a palavra com a quantidade
   de vezes que ela aperece.
   
   assinatura: string----> dicionário
   """
def separa_palavras(frases):
    frases1 = frases.split(' ')
    if frases1[0]==' ':
        del frases1[0]
    if frases1[-1]==' ':
        del frases1[-1]

def freq_palavras(frases):
    x=separa_palavras(frases)
    proximo=0
    contador_palavras= {}
    while(proximo <= len(x)):
        contador_palavras[x[proximo]]= x.count(x[proximo])
        proximo=proximo+1
    return contador_palavras