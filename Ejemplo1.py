print("Hola mundo, version 2.0")
n= input("Ingrese un numero menor a 10;  ")
n = int(n)
for i in range (1,n):
    if i % 2==0:
         print("El numero ", i, "es par ")
    else:
        print("El numero ", i, " es impar")
