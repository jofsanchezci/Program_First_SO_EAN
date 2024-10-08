import time

def facto(n):
	if n==0 or n==1:
		return 1
	else:
		return n*facto(n-1)

num=int(input('Ingrese el numero: '))

inicio=time.time()
a=facto(num)
fin=time.time()

tiempo=fin-inicio
print('El tiempo de ejecución es: ', tiempo, 's')
print('-----------------------------------')
print('El factorial es: ', a)
