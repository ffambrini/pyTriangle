import math

print "-----------------------------------------------------"
print "   A Formula de Heron calcula a area de um triangulo "
print "   em funcao das medidas dos seus tres lados.        "
print "-----------------------------------------------------"
print "                                                     "
print " Escrito por: Francisco Fambrini - 11/02/2017         "
print "     FESB - Faculdade de Engenharia Agronomica        "
print "     Versao 2.0 - calcula com 6 casas decimais        "
print "                                                      "

def main():
    
    n= raw_input("Digite a medida do Lado AB do Triangulo= ")
    AB = float(n)
    
    n= raw_input("Digite a medida do Lado BC do Triangulo= ")
    BC = float(n)

    n= raw_input("Digite a medida do Lado AC do Triangulo= ")
    AC = float(n)

    p= (AB+AC+BC) / 2    # p  é o semi-perimetro do Triangulo 

    A = p*(p-AB)*(p-AC)*(p-BC)

    AR = math.sqrt(A)
    
    print "                                                     "
    print 'A Area deste Triangulo vale: ', "%.6f"%AR
    print "                                                     "

#Calcula os angulos internos utilizando Lei dos Cossenos
    
    ang1 = math.acos ( ( BC**2 + AC**2 - AB**2 )/ (2*BC*AC))

    ang2 = math.acos ( ( AB**2 + AC**2 - BC**2 )/ (2*AB*AC))

    ang3 = math.acos ( ( AB**2 + BC**2 - AC**2 )/ (2*AB*BC))
    
    print "                                                     "

    
#Converte o angulo ang1  de radianos para graus e mostra o resultado:
#Observar o Codigo de Formataçao para a função print "%.2f"%
    
    print 'Os tres angulos internos deste triangulo, medem, em GRAUS:'
    print "                                                     "
    print  "%.6f"%math.degrees(ang1) 
    print "                                                     "
    print  "%.6f"%math.degrees(ang2) 
    print "                                                     "
    print  "%.6f"%math.degrees(ang3) 
    print "                                                     "

    
#Calculo das 3 Alturas do Triangulo
    h1 = 2*AR / AB
    h2 = 2*AR / AC
    h3 = 2*AR / BC

    print 'A Altura em relacao ao lado AB mede= ',"%.6f"%h1
    print "                                                     "

    print 'A Altura em relacao ao lado AC mede= ',"%.6f"%h2
    print "                                                     "

    print 'A Altura em relacao ao lado BC mede= ',"%.6f"%h3
    print "                                                     "

    input("Pressione ENTER para encerrar")



  
    
if __name__ == "__main__":
    main()
