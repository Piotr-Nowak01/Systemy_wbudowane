#Zadanie 1
s=input("Podaj ciąg znaków:\n")
hash_table={}
for char in s:
    if char in hash_table:
        hash_table[char]+=1
    else:
        hash_table[char]=1
print(hash_table)
#Zadanie 2
s=input("Podaj nazwę pliku, z którego ma być wyświetlony tekst. \n")
hash_table={}
print("Tekst oryginalny: \n")
with open (s) as f:
    for line in f:
        for char in line:
            print(char,end='')
            if char in hash_table:
                hash_table[char]+=1
            else:
                hash_table[char]=1
print("\n Tablica znaków: \n")
print(hash_table)
#Zadanie 3
tablica=[]
n=int(input("Ile liczb chcesz wprowadzić? \n"))
for i in range (0,n):
    nr=int(input("\n Podaj liczbę: "))
    tablica.append(nr)
m=min(tablica)
print("Najmniejsza liczba: ")
print(m)
print("\n Pozycja najmniejszej liczby: ")
print(tablica.index(m)+1)
