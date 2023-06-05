print("Hola mundo, version 1.0")
n= input("Ingrese un numero menor a 10")
n = int(n)
for i in range (1,n):
    print("El valor es",i)
    
    if i % 2==0:
         print("El numero es par ")
    else:
        print("El numero es impar")