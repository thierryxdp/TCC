def inverter(frase):
    f1=frase.replace("-"," ")
    f2=f1.replace(","," ")
    f3=f2.replace(":"," ")
    f4=f3.replace(";"," ")
    f5=f4.replace("."," ")
    f6=f5.replace("?"," ")
    f7=f6.replace("!"," ")
    f8=f7.lower()
    f9=str.split(f8)
    
    return f9[::-1]


frase1="– À noite, tu olharás as estrelas. Aquela onde moro é muito pequena para que eu possa te mostrar. É melhor assim. Minha estrela será para ti qualquer uma das estrelas. Assim, gostaria de olhar todas elas... Serão todas suas amigas. E, também, eu lhe darei um presente..."
inverter(frase1)