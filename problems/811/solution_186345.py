# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''dados os parametros de entrada, compostos por uma lista com as dimensoes do colchao em centimetros da menor para a maior, e dois inteiros representando a altura da porta<H> e a largura da porta <L>; [int,int,int],int,int -> boolean''' 
    hporta = H
    lporta = L
    mcolchao = medidas
    hcolchao = mcolchao[0]
    lcolchao = mcolchao[1]
    ccolchao = mcolchao[2]
    if hporta < ccolchao and lporta < lcolchao and hporta < lcolchao:
        return False
    else:
        return True