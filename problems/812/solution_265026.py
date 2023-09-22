def sempontuacao ( frase ):
sem_pts = str.replace ( str.replace ( str.replace ( frase ,","," ") ,"."," ") ," ... "," ")
sem_pts2 = str.replace ( str.replace ( str .replace ( sem_pts ,"!"," ") ,"?"," ") ,";"," ")
return str.replace ( str.replace ( sem_pts2 , ":", " ") , "-"," ")