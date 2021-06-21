
class Formulario_Generador:

    def menuPrincipal(self):
        continuar=True
        while(continuar):
            opcionCorrecta=False
            while(not opcionCorrecta):
                print("==========================MENÚ PRINCIPAL==========================")
                print("1.- GENERAR CONTRASEÑA")
                print("2.- BUSCAR CONTRASEÑA")
                print("3.- ELIMINAR CONTRASEÑA")
                print("4.- FINALIZAR PROGRAMA")
                print("===================================================================")
                opcion=int(input("Seleccion una opción: "))
                
                if opcion<1 or opcion>4:
                    print("Opción incorrecta, ingrese nuevamente...")
                elif opcion==4:
                    continuar=False
                    print(" ¡Gracias por usar el sistema! ")
                    break
                else:
                    opcionCorrecta=True
                    ejecutarOpcion(opcion)

aplicacion1=Formulario_Generador()
aplicacion1.menuPrincipal()
               