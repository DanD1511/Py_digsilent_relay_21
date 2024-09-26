import cmath
import os
import sys

os.environ["PATH"] = r"C:\\Program Files\\DIgSILENT\\PowerFactory 2021 SP2" + ";" + os.environ["PATH"]
sys.path.append(r'C:\\Program Files\\DIgSILENT\\PowerFactory 2021 SP2\\Python\\3.9')

import powerfactory


class Line:
    def __init__(self, app, line_name):
        self.app = app
        self.line_name = line_name
        self.line_attributes = {}

    def __get_line__(self) -> powerfactory.DataObject:
        lines = self.app.GetCalcRelevantObjects('*.ElmLne')
        return [line for line in lines if line.loc_name == self.line_name][0]

    def get_line_attributes(self) -> dict:
        line = self.__get_line__()
        print(line)
        # Parámetros de la línea

        R1 = line.GetAttribute('R1')
        X1 = line.GetAttribute('X1')
        R0 = line.GetAttribute('R0')
        X0 = line.GetAttribute('X0')

        # Impedancia de secuencia positiva en forma rectangular
        Z1 = complex(R1, X1) # Z1 = R1 + jX1
        Z1 = list(cmath.polar(Z1))

        # Impedancia de secuencia cero en forma rectangular
        Z0 = complex(R0, X0)  # Z0 = R0 + jX0
        Z0 = list(cmath.polar(Z0))

        # Guardar los atributos en el diccionario para acceso posterior
        self.line_attributes = {
            'name': line.loc_name,
            'Z1': Z1,
            'Z0': Z0,
        }

        return self.line_attributes
