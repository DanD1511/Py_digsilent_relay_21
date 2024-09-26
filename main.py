from pprint import pprint

from line_model import Line
from powerfactory_application import App

project_name = 'Taller1_protecciones_DaCunhaVillalba'  # Nombre del proyecto

# Obtener aplicación de DigSilent
app = App(project_name)

# Obtener líneas de interés

lines_name = {
    'line_name_zone_1': 'LHV3',  # Línea donde se conecta la protección para la zona 1
    'line_name_zone_2': 'LHV1',  # Línea más corta para la zona 2
    'line_name_zone_3': 'LHV2'  # Línea más larga para la zona 3
}

lines = []
lines_attributes = {}

for line_name in lines_name.values():
    line = Line(app=app.app, line_name=line_name)  # Instancia de la clase línea
    lines.append(line)

# Obtener los atributos de las líneas

for line in lines:
    line_attributes = line.get_line_attributes()
    lines_attributes[line_attributes['name']] = line_attributes

pprint(lines_attributes)

# TODO: IMPEDANCIAS PARA LA CONFIGURACIÓN DE LA PROTECCIÓN 21 FASE - FASE

# Líneas

line_zone_1 = lines_name['line_name_zone_1']
line_zone_2 = lines_name['line_name_zone_2']
line_zone_3 = lines_name['line_name_zone_3']

# Impedancias de líneas

z_l1_p_p = lines_attributes[line_zone_1]['Z1'][0] * 0.8
z_l2_p_p = lines_attributes[line_zone_2]['Z1'][0] * 0.5
z_l3_p_p = lines_attributes[line_zone_3]['Z1'][0] * 0.25

# Zona 1 p-p

# Es igual al 80% de la impedancia de la línea

# Cálculo de la impedancia corregida para la zona 1 (fase - fase)

z_zone_1_p_p = z_l1_p_p
print("Impedancia de la zona 1 (fase - fase): ", z_zone_1_p_p)

# Zona 2 p-p

# Es igual a: z_l1_p_p + 0.5 * z_l2_p_p(más corta)

# Cálculo del factor de corrección

i_rele = 0.416  # Corriente del relé en kA
i_infeed = 2.910  # Corriente infeed total (IA + IB) en kA
k_2 = i_infeed / i_rele

# Cálculo de la impedancia corregida para la zona 2 (fase - fase)

z_zone_2_p_p = z_zone_1_p_p + k_2 * z_l2_p_p
print("Impedancia de la zona 2 (fase - fase): ", z_zone_2_p_p)

# Zona 3 p-p

# Cálculo del factor de corrección

i_rele = 1.098  # Corriente del relé en kA
i_b = 0.346  # Corriente infeed de la zona 2
i_c = 2.446  # Corriente infeed de la zona 3

k1 = i_b / i_rele
k3 = i_c / i_rele
k2 = k1 + k3

# Cálculo de la impedancia corregida para la zona 3 (fase - fase)

z_zone_3_p_p = z_zone_1_p_p + z_zone_2_p_p * (1 + k1) + z_l3_p_p * (1 + k2)
print("Impedancia de la zona 3 (fase - fase): ", z_zone_3_p_p)


# TODO: IMPEDANCIAS PARA LA CONFIGURACIÓN DE LA PROTECCIÓN 21 FASE - TIERRA

# Zona 1 p-e

# Cálculo de la impedancia corregida para la zona 1 (fase - tierra)

z_zone_1_p_e = z_l1_p_p
print("Impedancia de la zona 1 (fase - tierra): ", z_zone_1_p_e)

# Zona 2 p-e

# Es igual a: z_l1_p_p + 0.5 * z_l2_p_p(más corta)

# Cálculo del factor de corrección

i_rele = 0.024  # Corriente del relé en kA
i_infeed = 0.612  # Corriente infeed total en kA
k_2 = i_infeed / i_rele

# Cálculo de la impedancia corregida para la zona 2 (fase - tierra)

z_zone_2_p_e = z_zone_1_p_e + k_2 * z_l2_p_p
print("Impedancia de la zona 2 (fase - tierra): ", z_zone_2_p_e)

# Zona 3 p-e

# Cálculo del factor de corrección

i_rele = 0.062  # Corriente del relé en kA
i_b = 0.088  # Corriente infeed de la zona 2
i_c = 0.286  # Corriente infeed de la zona 3

k1 = i_b / i_rele
k3 = i_c / i_rele
k2 = k1 + k3

# Cálculo de la impedancia corregida para la zona 3 (fase - tierra)

z_zone_3_p_e = z_zone_1_p_e + z_zone_2_p_e * (1 + k1) + z_l3_p_p * (1 + k2)
print("Impedancia de la zona 3 (fase - tierra): ", z_zone_3_p_e)

