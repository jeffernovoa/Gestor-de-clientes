import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
import gestor.app_config as config

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"
    
class Clientes:
    # Creamos la lista y cargamos los clientes en memoria
    lista = []
    if not os.path.exists(config.DATABASE_PATH):
        # Crear el archivo vacío si no existe
        with open(config.DATABASE_PATH, "w") as fichero:
            pass

    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for c in Clientes.lista:
                writer.writerow((c.dni, c.nombre, c.apellido))

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
            
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[i]
            
    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(i)
                Clientes.guardar()
                return cliente
            