import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
import gestor.app_config as config

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "clientes.csv")

if 'pytest' in os.path.basename(__file__):
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "tests", "clientes_test.csv")

def test_escritura_csv(self):
    db.Clientes.borrar('48H')
    db.Clientes.borrar('15J')
    db.Clientes.modificar('28Z', 'Mariana', 'Pérez')

    dni, nombre, apellido = None, None, None
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        dni, nombre, apellido = next(reader)  # Primera línea del iterador

    self.assertEqual(dni, '28Z')
    self.assertEqual(nombre, 'Mariana')
    self.assertEqual(apellido, 'Pérez')