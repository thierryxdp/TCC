#Start your python function here
def filtra_pares (a,b,c,d):
    """ Retorna os valores pares na lista a,b,c,d em uma nova lista, list->list """
    resultado1=a%2;
    resultado2=b%2;
    resultado3=c%2;
    resultado4=d%2;
    if (resultado1==0 and resultado2!=0 and resultado3!=0 and resultado4!=0):
        return (a);
    else:
        if (resultado1==0 and resultado2==0 and resultado3!=0 and resultado4!=0):
            return (a,b);
        if (resultado1==0 and resultado2!=0 and resultado3==0 and resultado4!=0):
            return (a,c);
        if (resultado1==0 and resultado2!=0 and resultado3!=0 and resultado4==0):
            return (a,d);
        if (resultado1!=0 and resultado2==0 and resultado3==0 and resultado4!=0):
            return (b,c);
        if (resultado1!=0 and resultado2==0 and resultado3!=0 and resultado4==0):
            return(b,d);
        if (resultado1!=0 and resultado2!=0 and resultado3==0 and resultado4==0):
            return(c,d);
        if (resultado1==0 and resultado2==0 and resultado3==0 and resultado4==0):
            return(a,b,c,d);
        if (resultado1!=0 and resultado2!=0 and resultado3!=0 and resultado4!=0):
            return();
        if (resultado1==0 and resultado2==0 and resultado3==0 and resultado4!=0):
            return "(a,b,c)";
        if (resultado1==0 and resultado2==0 and resultado3!=0 and resultado4==0):
            return(a,b,d);
        if (resultado1==0 and resultado2!=0 and resultado3==0 and resultado4==0):
            return(a,c,d);
        if (resultado1!=0 and resultado==0 and resultado3==0 and resultado4==0):
            return(b,c,d);