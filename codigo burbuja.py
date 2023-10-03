longitud = [5, 3, 8, 4, 6]

#Este for nos sirve para iterar cada uno de los elementos del arreglo ya definido
 #el menos 1 es por que como compara cada elemnto del arreglo, no tiene caso que compare el ultimo

band = False
#esto es para que siga comparando siempre y cuando siga dsordenado
while band == False:
    #esto es para cuando ya este ordenado
    band == True
for i in range(len(longitud)-1):
    #interar,si la lista en esta posicion es mayor al que esta en la derecha, entonces entra a la condición, por que esta desordenando.
    if longitud[i] > longitud[i + 1]:
        #variable para guardar el elemento
        aux = longitud[i]
        #ahora hago un intercambio para que lo ordene
        longitug[i] =  longitud[i + 1]
        #cambio la condición
        longitud[i + 1] = aux
        #esto indica que sigue desordenado
        band= False

#inprimo el arreglo, fuera del for.
print(longitud)
    