from stark import lista_personajes

correr = True

while(correr):

    respuesta = int(input("\nMenu de opciones:\n"
                "1-Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe\n"
                "2-Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza \n"
                "3-Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo\n"
                "4-Recorrer la lista y determinar el peso promedio de los superhéroes masculinos\n"
                "5-Recorrer la lista y mostrar nombre y peso de los superhéroes los cuales su fuerza "
                "supere a la fuerza promedio de todas las superhéroes de género femenino\n"
                "6-Salir\n"))

    match(respuesta):
        case 1:
            for element in lista_personajes:
                print(element)
        case 2:
            maximo_peso = None
            for element in lista_personajes:
                if maximo_peso == None or float(element['fuerza']) >  maximo_peso:

                    maximo_peso = float(element['fuerza']) 
                    peso_del_maximo = element['peso']
                    identidad_del_maximo = element['identidad']
                elif float(element['fuerza']) == maximo_peso:
                    peso_del_segundo = element['peso']
                    identidad_del_segundo = element['identidad']                   
                
            print(f"El sprimer super heroe con más fuerza es {identidad_del_maximo} y su peso es de {peso_del_maximo}")
            print(f"El segundo heroe con más fuerza es {identidad_del_segundo} y su peso es de {peso_del_segundo}")
        case 3:
            minimo_altura = None
            for element in lista_personajes:
                if minimo_altura == None or float(element['altura']) <  minimo_altura:
                    minimo_altura = float(element['altura']) 
                    nombre_mas_bajo = element['nombre']
                    identidad_mas_bajo = element['identidad']
                
            print(f"El sprimer super heroe es {nombre_mas_bajo} y su identidad es {identidad_mas_bajo}")
        case 4:
            contador_peso = 0
            contador_masculinos = 0
            for element in lista_personajes:
                if element['genero'] == "M":
                    contador_peso = contador_peso + float(element['peso'])
                    contador_masculinos = contador_masculinos + 1

            peso_promedio =contador_peso/contador_masculinos
            print(f"El peso promedio de los masculinos es {peso_promedio}")

        case 5:
            contador_femeninas = 0
            contador_fuerza = 0
            for element in lista_personajes:
                if element['genero'] == "F":
                    contador_femeninas = contador_femeninas + 1
                    contador_fuerza = contador_fuerza + float(element['fuerza'])

            promedio_fuerza = contador_fuerza/contador_femeninas

            for element in lista_personajes:
                if element['genero'] == "M" and float(element['fuerza']) > promedio_fuerza:
                    print(f"El nombre es {element['nombre']} y su peso {element['peso']}")

            print(promedio_fuerza)
        case 6:
            break
