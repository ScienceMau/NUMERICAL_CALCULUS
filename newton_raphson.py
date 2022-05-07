import matplotlib.pyplot as plt
import numpy as numpy

### FUNÇÂO A SER ENCONTRADA A RAIZ
def f(x):
    y = x**3-5*x-9
    return y

##DERIVADA DA FUNçÂO
def df(x):
    dy =  3*x**2-5
    return dy


### ORGANIZA O TEXTO
def texto_legal(frase):
    print("*"*len(frase))
    print(frase)
    print("*"*len(frase))
    

### FUNÇÂO DO METODO DE NEWTON RAPHSON
def NR(x0,e,N):

    texto_legal("METODO DE NEWTON-RAPHSON")

    step = 1
    flag = 1
    condition = True
    while condition:
        if df(x0) == 0:
            print("ERRO, divisão por zero!")
            break
        x1 = x0 -f(x0)/df(x0)
        print('Iteração %d, x1 = %0.6f and f(x1) = %0.6f' %(step,x1,f(x1)))
        x0   = x1
        step = step +1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e
    
    if flag == 1:
        texto_legal(' A raiz aproximada é: %0.6f' %x1)
    else :
        texto_legal(' Não converge.')



### NR(valor de aproximação, convergencia, numero de interações)
NR(3,1e-8,1000)