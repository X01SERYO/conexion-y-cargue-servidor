import pandas as pd
import numpy as np
from conexion_a_servidor import *


def procesamiento():
    df = pd.read_excel(r'D:\Sergio\Documents\Python\Proyectos\Conexion a servidor\usuarios.xlsx', dtype={'cedula': str})

    insert = """INSERT INTO public.usuarios
    (fecha, cedula, nombre, apellido, direccion, telefono, created_by)
    VALUES(%s, %s, %s, %s, %s, %s, %s);
    """

    delete = False

    return load(df, delete, insert)


if __name__ == '__main__':
    print(procesamiento())
