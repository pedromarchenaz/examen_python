# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:20:40 2021

@author: PedroLuis
"""

# Ejercicio 1
nkilo = float(input('Digite la cantidad de kilo: '))

if nkilo >= 0 and nkilo < 2:
    print('Tiene un descuento del 0%')
if nkilo >= 2 and nkilo < 5:
    print('Tiene un descuento del 10%')
if nkilo >= 5 and nkilo < 10:
    print('Tiene un descuento del 15%')
if nkilo >= 10:
    print('Tiene un descuento del 20%')


# Ejercicio 2
200

# Ejercicio 3
marcaap = input('Digite la marca del aparato: ')
valorap = float(input('Digite el valor del aparto: $'))

if valorap >= 4000:
    desc1 = valorap * 0.20
if marcaap == 'nosy':
    desc2 = valorap * 0.10

totaldesc = desc1 + desc2
vcondesc = valorap - totaldesc
taparato = vcondesc + (vcondesc * 0.30)

print(f'El valor a pagar del aparato con iva incluido es : ${taparato:,} ')


# Ejercicio 4
nhecta = float(input('Digite la cantidad de hectareas: '))

if nhecta > 5:
    print('Aplica el 80% para pino')
    print('Aplica el 15% para oyamel')
    print('Aplica el 5% para cedro')
    hp = nhecta * 0.80
    ho = nhecta * 0.15
    hc = nhecta * 0.05

if nhecta <= 5:
    print('Aplica el 45% para pino')
    print('Aplica el 25% para oyamel')
    print('Aplica el 30% para cedro')
    hp = nhecta * 0.45
    ho = nhecta * 0.25
    hc = nhecta * 0.30

print('La cantidad a sembrar de pino es de: ', hp, ' hectareas.')
print('La cantidad a sembrar de oyamel es de: ', ho, ' hectareas.')
print('La cantidad a sembrar de cedro es de: ', hc, ' hectareas.')


# Ejercicio 5
numuno = int(input('Digite número 1: '))
numdos = int(input('Digite número 2: '))
numtres = int(input('Digite número 3: '))

if numuno > numdos and numuno > numtres:
    print('El numero 1 es mayor :', numuno)
if numdos > numuno and numdos > numtres:
    print('El numero 2 es mayor :', numdos)
if numtres > numdos and numtres > numuno:
    print('El numero 3 es mayor :', numtres)
