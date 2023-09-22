def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra é uma chave e o número
    de vezes que aparece é o seu valor
    assinatura: string --> dic
    
    Mais uma complicação com algo trivial, e a falta de atenção fez perder
    muito tempo testando outros possíveis problemas como o filtro split, enquan-
    to o real era o prefixo de '.count', que devia ser a 'lista' filtrada pelo
    split, e eu estava usando o frases, argumento puro...
    
    Após uma revisão ainda não entendo o porquê dos códigos de erro ao tentar usar o update 
    com um dicionário vazio por tanto tempo, mas suspeito que era um erro de sintaxe meu
    """
    dic={}
    lista=frases.split(' ')
    for i in range(len(lista)):
    	dic.update({lista[i] : lista.count(lista[i])})
         	  
    return dic