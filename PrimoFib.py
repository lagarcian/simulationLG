# Python 3 Programa para imprimir los numeros primos en la serie Fibonacci
import math 
  
# Funcion para chequear si el numero es cuadrado perfecto 
def esCuadrado(n) : 
    raiz = (int)(math.sqrt(n)) 
    return (raiz * raiz == n) 
  
  
# Imprime todos los numeros que son menores o iguales que n y que son primos.  
def imprimirPrimoFib(n) : 
      
    # Usando condicionales para generar los primos menores o iguales a n.  
    primo =[True] * (n + 1)  
    p = 2
    while(p * p <= n ): 
          
        # si primo[p] no cambia, 
        # entonces es un primo 
        if (primo[p] == True) : 
              
            # Actualiza todos los multiplos de p 
            for i in range(p * 2, n + 1, p) : 
                primo[i] = False
                  
        p = p + 1
      
    # Ahora recorre todos los numeros primos y mira cual es Fibonnaci
    for i in range(2, n + 1) : 
        if (primo[i] and (esCuadrado(5 * i * i + 4) > 0 or
             esCuadrado(5 * i * i - 4) > 0)) : 
            print(i , " ",end="") 
  
  

n = 30
imprimirPrimoFib(n); 
  
  
#Luis García