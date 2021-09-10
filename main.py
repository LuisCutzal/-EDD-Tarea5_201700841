from Analizadores.Sintactico import parser
from Analizadores.Sintactico import tipo
from Estudiantes import Estudiante
from Tareas import Tarea
if __name__ == '__main__':
    f=open('SalidaSmartClass.txt',"r", encoding="utf-8")
    mensaje=f.read()
    f.close()
    parser.parse(mensaje)
    lest=list()
    ltar=list()
    for i in range(len(tipo)):
        if tipo[i] == "user":
            NE = Estudiante(tipo[i+1],tipo[i+2],tipo[i+3],tipo[i+4],tipo[i+5],tipo[i+6],tipo[i+7],tipo[i+8])
            lest.append(NE)
        if tipo[i]=="task":
            NT = Tarea(tipo[i+1],tipo[i+2],tipo[i+3],tipo[i+4],tipo[i+5],tipo[i+6],tipo[i+7])
            ltar.append(NT)

    print("ESTUDIANTES")
    for a in range(len(lest)):
        print("Carnet: ",lest[a].carnet)
        print("DPI: ",lest[a].dpi)
        print("Nombre: ",lest[a].nombre)
        print("Carrera: ",lest[a].carrera)
        print("Correo: ",lest[a].correo)
        print("Contraseña: ",lest[a].password)
        print("Creditos: ",lest[a].creditos)
        print("Edad: ",lest[a].edad)
    
    print("TAREAS")
    for b in range(len(ltar)):
        print("Carnet: ",ltar[b].carnet)
        print("Nombre: ",ltar[b].Nombre)
        print("Descripcion: ",ltar[b].Descripcion)
        print("Materia: ",ltar[b].Materia)
        print("Fecha: ",ltar[b].Fecha)
        print("Hora: ",ltar[b].Hora)
        print("Estado: ",ltar[b].Estado)