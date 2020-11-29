#Matteo Crisafulli [TechTheGuy]
#Programma per la conversione di un numero da decimale a binario con
#l'algoritmo della divisione


print("dammi il numero")

#funzione flippa
def flippa(x):
  return x[::-1]

#dichiara varaibli
n = int(input())
t1 = int(n)
t2 = int(n%2)

ris = ""
riscon = ""

print("Risolvo:")

#calcola

while t1 != 0 :
	print(str(t1) +  ":2=" +  str(int(t1//2)) + " R" + str(t1%2))
	t2 = int(t1%2)
	t1 = int(t1//2)
	ris = ris + str(t2)
riscon = flippa(ris)


print(str(n) + "=" + riscon)
