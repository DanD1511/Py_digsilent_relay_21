import os
import sys
from pprint import pprint

from line_model import Line

os.environ["PATH"] = r"C:\\Program Files\\DIgSILENT\\PowerFactory 2021 SP2" + ";" + os.environ["PATH"]
sys.path.append(r'C:\\Program Files\\DIgSILENT\\PowerFactory 2021 SP2\\Python\\3.9')

import powerfactory as pf


class App:
    def __init__(self, project_name):
        self.app = self.__get_app__()
        self.__project_init__(project_name)  # Activar proyecto

    @staticmethod
    def __get_app__():
        return pf.GetApplication()

    def __project_init__(self, project_name):
        self.app.ActivateProject(project_name)
