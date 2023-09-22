def  intercalando_listas ( lista1 , lista2 ):
    retornar  zip ( lista1 , lista2 )

if  __name__  ==  '__main__' :
    print ( "Exc1 conta_palavras" , conta_palavras ( "hola Susana te estamos llamando queremos jugar" ))
    print ( "Exc2 retirar" , retirar ( "Hola Susana te estamos llamando queremos llamando" , "llamando" , 10 , 48 ))
    print ( "Exc3 substituir" , substituir_espaco ( "Hola Susana te estamos llamando queremos llamando" ))
    print ( "Exc4 apos_chr" , apos_chr ( "Hola Susana te estamos llamando queremos llamando" , "na" ))
    print ( "Exc6 intercalando_listas" , intercalando_listas ([ 1 , 3 , 5 ], [ 2 , 4 , 6 ]))