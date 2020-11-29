#Matteo Crisafulli [TechTheGuy]
#Programma per la conversione di un numero da decimale a binario con
#l'algoritmo della divisione

#input
n = int(input("Dammi il numero: "))
base = int(input("Dammi la base: "))
#funzione flippa
def flippa(x):
  return x[::-1]

#dichiara varaibli
t1 = int(n)
t2 = int(n%base)

ris = ""
riscon = ""

print("Risolvo:")

#calcola

while t1 != 0 :
	print(str(t1) +  ":" + str(base) + "= " +  str(int(t1//base)) + " R" + str(t1%base))
	t2 = int(t1%base)
	t1 = int(t1//base)
	ris = ris + str(t2)
riscon = flippa(ris)

#print(" ecco il risultato")

print(str(n) + "=" + riscon)
