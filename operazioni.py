#Matteo Crisafulli [TechTheGuy]
#Programma per la conversione di un numero da decimale a binario con
#l'algoritmo della divisione


operando1 = int(input("first operand: "))
segno = str(input("sign: + - :  "))
operando2 = int(input("second operand: "))
if segno == "+" :
	risoper = int(str(operando1), 2) + int(str(operando2), 2)
if segno == "-" :
	risoper = int(str(operando1), 2) - int(str(operando2), 2)
n = bin(risoper)

print(str(operando1) + str(segno) + str(operando2) + "=" +  str(n))
