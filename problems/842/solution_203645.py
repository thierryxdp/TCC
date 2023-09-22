'Cria função que retorna times e pontuações após 2 partidas. entrada de 2 listas e saída de um dicionário'
def pontos_por_time (tabela)
jogo1=(lista[0])
jogo2=(lista[1])
time1=(jogo1[0])
time2=(jogo1[1])
placarjogo1=(jogo1[2])
placarjogo1a=(placarjogo1[0])
placarjogo1b=(placarjogo1[1])
placarjogo2=(jogo2[2])
placarjogo2a=(placarjogo2[0])
placarjogo2b=(placarjogo2[1])
pontuacaotime1=0
pontuacaotime2=0
if placarjogo1a>placarjogo1b:
    pontuacaotime1=pontuacaotime1 + 3
elif placarjogo1a==placarjogo1b:
    pontuacaotime1=pontuacaotime1 + 1 
elif placarjogo1a<placarjogo1b:
    pontuacaotime2=pontuacaotime2 + 3
if placarjogo2a>placarjogo2b:
    pontuacaotime2=pontuacaotime2 + 3
elif placarjogo2a==placarjogo2b:
    pontuacaotime1=pontuacaotime1 + 1
if placarjogo2a==placarjogo2b:
    pontuacaotime2=pontuacaotime2 + 1
elif placarjogo2a<placarjogo2b:
    pontuacaotime2=pontuacaotime2 + 3
def pontos_por_time (tabela):
    resultado={time1:pontuacaotime1, time2:pontuacaotime2} 
    tabela=(resultado)
    return (resultado)