def colchao_passa (dimensoes_colchao, dimensoes_porta) :
    ''' funçao que define se o colchao passa pela porta ou não, dados suas respectivas medidas'''
   
   <<< dimensoes_colchao = [A,B,C]
   <<< dimensoes_colchao = [60,200,230]
   <<< dimensoes_porta = [100,220]
       if C > 220 :
       return 'False'
       else :
       return 'True'# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis