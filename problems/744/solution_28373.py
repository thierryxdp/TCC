def hashtag(s):
    """Funcao que recebe uma string s e retorna a mesma string com o 
    caractere "#" no inicio, no meio e no final dela. Por exemplo, se a
    entrada for "abcd", a saida deve ser "#ab#cd#". Outro exemplo: se
    receber "abcde", a funcao deve retornar "ab#cde#";
    str->str"""
    var=int(len(s)//2)
	return "#"+s[0:var]+"#"+s[var:]+"#"