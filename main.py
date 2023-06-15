from Persona import *
import numpy as np
import random as rn
arreglo_personas=np.array([])

ciclo=True


def agregarPersona(arreglo_personas):
    p = Persona()

    c = False
    while c == False:
        c = p.setNIF(input("Ingrese NIF Ej.99999999-AAA:"))
    c = False
    while c == False:
        c = p.setNombre(input("Ingrese Nombre:"))
    c = False
    while c == False:
        try:
            c = p.setEdad(int(input("Ingrese Edad:")))
        except BaseException as error:
            print(f"Error:{error}")
    return np.append(arreglo_personas , p)


def buscarPersona(arreglo_personas):
    nif = input("Ingrese NIF:")
    flag = False
    for persona in arreglo_personas:
        if nif == persona.NIF:
            flag = True
            print("Datos del Ciudadano")
            print(f"NIF   :{persona.NIF}")
            print(f"Nombre:{persona.Nombre}")
            print(f"Edad  :{persona.Edad}")
            if persona.Edad >=15:
                print("Pertenece UE")
            else:
                print("No Pertenece UE")
    if flag == False:
        print("persona no existe")


def imprimirCertificado(arreglo_personas):
    nif = input("Ingrese NIF:")
    flag = False
    for persona in arreglo_personas:
        if nif == persona.NIF:
            flag = True
            aleatorio = rn.randint(1,3)
            match aleatorio:
                case 1:
                    print("Certificado de Nacimiento")
                case 2:
                    print("Certificado Conyugal")
                case 3:
                    print("Certificado UE")
            print(f"NIF   :{persona.NIF}")
            print(f"Nombre:{persona.Nombre}")
            print(f"Edad  :{persona.Edad}")
            if persona.Edad >= 15:
                print("Pertenece UE")
            else:
                print("No Pertenece UE")
    if flag == False:
        print("persona no existe")


def salir():
    print("CopyRigth: Juanito Simio INC. 2023")
    return False


while ciclo:
    print("Menu Principal NIF UE")
    print("1) Registrar Persona")
    print("2) Buscar Persona")
    print("3) Imprimir Certificado")
    print("4) Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                print("Registrar Persona")
                arreglo_personas = agregarPersona(arreglo_personas)
            case 2:
                print("Buscar Persona")
                buscarPersona(arreglo_personas)
            case 3:
                print("Imprimir Certificado")
                imprimirCertificado(arreglo_personas)
            case 4:
                print("Salir")
                ciclo = salir()
            case _:
                print("seleccion invalida")
    except BaseException as error:
        print(f"Error:{error}")