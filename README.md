# Revisiones técnico-mecánicas

## Grupo

* Luis Alejandro Mongua López [lamongual@unal.edu.co](lamongual@unal.edu.co)
* Ivanhoe Rozo Rojas [irozor@unal.edu.co](irozor@unal.edu.co)
* Camilo Alfonso Mosquera Benavides [camosquerab@unal.edu.co](camosquerab@unal.edu.co)

## Descripción general del dataset

El dataset corresponde a los resultados de las revisiones técnico-mecánicas de varias topologías de vehículos en CDAs (Centros de Diagnóstico Automotor) en todo el país entre los años 2014 y 2022, incluye algunos valores cualitativos y otros cuantitativos. La cantidad de registros se estima en 9'000.000, organizados en 35 variables.

Es de anotar que algunos datos no aplican para algunos tipos de vehículo, por ejemplo, las motocicletas no cuentan con valores cuantitativos del estado de la suspensión, y los vehículos que funcionan con combustible diesel no tienen valores en los campos de emisiones de HC, CO, CO2 ni O2 (sus emisiones se miden en porcentaje de opacidad)

Los datos fueron extraídos de la base de datos de inspecciones de varios CDA y fueron anonimizados para no violar las políticas de privacidad y protección de datos personales.

## Objetos

Cada registro (objeto) del dataset corresponde a una revisión completa de un vehículo automotor, el concepto final de la revisión puede ser "aprobado" (codificado con un 1) o "rechazado" (codificado con un 2) de acuerdo con los criterios de la norma técnica colombiana NTC 5375.

De acuerdo con la normatividad colombiana, los vehículos automotores que obtengan un concepto de "rechazado" en su inspección, cuentan con un periodo de gracia de 15 días calendario para realizar las reparaciones correspondientes y realizar nuevamente la inspección sin costo en el mismo centro de diagnóstico. 

## Variables

### adherencia__eje1__de

Porcentaje de adherencia de la llanta derecha del eje delantero, valor en porcentaje de adherencia, con rango entre 0 y 100, de tipo ratio. Tipo de dato: Punto flotante. 

### adherencia__eje1__iz

Porcentaje de adherencia de la llanta izquierda del eje delantero, valor en porcentaje de adherencia, con rango entre 0 y 100, de tipo ratio. Tipo de dato: Punto flotante.

### adherencia__eje2__de

Porcentaje de adherencia de la llanta derecha del eje trasero, valor en porcentaje de adherencia, con rango entre 0 y 100, de tipo ratio. Tipo de dato: Punto flotante.

### adherencia__eje2__iz

Porcentaje de adherencia de la llanta izquierda del eje trasero, valor en porcentaje de adherencia, con rango entre 0 y 100, de tipo ratio. Tipo de dato: Punto flotante.

### desviacion_lateral__eje1

Desviación lateral (convergencia o divergencia) de las llantas del eje delantero, valor en m/km, rango entre -40 y 40, de tipo ratio. Tipo de dato: punto flotante. 

### desviacion_lateral__eje2

Desviación lateral (convergencia o divergencia) de las llantas del eje trasero, valor en m/km, rango entre -40 y 40, de tipo ratio. Tipo de dato: punto flotante. 

### frenos__eficacia_total

Eficacia de frenado, corresponde a la suma de todas las fuerzas de frenado del freno principal de servicio dividida entre la suma de los pesos. Valor en porcentaje, rango entre 0 y 100, de tipo ratio. Tipo de dato: punto flotante. 

### frenos__eficacia_auxiliar

Eficacia de frenado del freno auxiliar, corresponde a la suma de todas las fuerzas de frenado del freno auxiliar dividida entre la suma de los pesos. Valor en porcentaje, rango entre 0 y 100, de tipo ratio. Tipo de dato: punto flotante.

### frenos__desequilibrio_eje_1

Desequilibrio entre las fuerzas de frenado del eje delantero, corresponde a la fuerza máxima en el eje delantero dividida entre la suma de las fuerzas del eje delantero. Valor en porcentaje, rango entre 0 y 100, de tipo ratio. Tipo de dato: punto flotante.

### frenos__desequilibrio_eje_2

Desequilibrio entre las fuerzas de frenado del eje trasero, corresponde a la fuerza máxima en el eje trasero dividida entre la suma de las fuerzas del eje trasero. Valor en porcentaje, rango entre 0 y 100, de tipo ratio. Tipo de dato: punto flotante.

### gases__opacidad_promedio

Valor del promedio aritmético de las aceleraciones en los ciclos 2, 3 y 4 de la prueba de opacidad realizada con los procedimientos definidos en la norma técnica colombiana NTC4231, valor en porcentaje de opacidad, rango entre 0 y 100, de tipo ratio. Tipo de dato: punto flotante.

### gases__ralenti__co

Valor de la concentración de monóxido de carbono durante la prueba de emisiones contaminantes a velocidad ralentí de acuerdo con los procedimientos definidos en la norma técnica colombiana NTC4983 (o NTC5365 en el caso de motocicletas), valor en porcentaje, rango entre 0 y 100 de tipo ratio. Tipo de dato: punto flotante. 

### gases__ralenti__co2

Valor de la concentración de dióxido de carbono durante la prueba de emisiones contaminantes a velocidad ralentí de acuerdo con los procedimientos definidos en la norma técnica colombiana NTC4983 (o NTC5365 en el caso de motocicletas), valor en porcentaje, rango entre 0 y 100 de tipo ratio. Tipo de dato: punto flotante. 

### gases__ralenti__hc

Valor de la concentración de hidrocarburos durante la prueba de emisiones contaminantes a velocidad ralentí de acuerdo con los procedimientos definidos en la norma técnica colombiana NTC4983 (o NTC5365 en el caso de motocicletas), valor en partes por millón (ppm), rango entre 0 y 30000 de tipo ratio. Tipo de dato: entero. 

### gases__ralenti__o2

Valor de la concentración de oxígeno durante la prueba de emisiones contaminantes a velocidad ralentí de acuerdo con los procedimientos definidos en la norma técnica colombiana NTC4983 (o NTC5365 en el caso de motocicletas), valor en porcentaje, rango entre 0 y 100, de tipo ratio. Tipo de dato: punto flotante. 

### luces__intensidad__total

Suma de las intensidades de las luces que se pueden encender simultaneamente, valor en klux a 1m, con rango entre 0 y 600 de tipo ratio. Tipo de dato: punto flotante.

### taxi__error_distancia

Error entre el valor en distancia medido por el taxímetro del vehículo y el valor de referencia. Valor en porcentaje, con rango entre -100 % y 100% de tipo ratio. Tipo de dato: punto flotante.

### taxi__error_tiempo

Error entre el valor en tiempo medido por el taxímetro del vehículo y el valor de referencia. Valor en porcentaje, con rango entre -100 % y 100% de tipo ratio. Tipo de dato: punto flotante.

### luces__inclinacion__baja1_de

Inclinación de la primera luz derecha respecto a la horizontal. Valor en porcentaje de inclinación (tangente_inversa(angulo_de_inclinacion) * 100 %), con rango entre -15 y 15 de tipo ratio. Tipo de dato: punto flotante. 

### luces__inclinacion__baja1_iz

Inclinación de la primera luz izquierda respecto a la horizontal. Valor en porcentaje de inclinación (tangente_inversa(angulo_de_inclinacion) * 100 %), con rango entre -15 y 15 de tipo ratio. Tipo de dato: punto flotante. 

### luces__intensidad__baja1_de

Intensidad de la primera luz baja del lado derecho, valor en klux a 1m, con rango entre 0 y 300 de tipo ratio. Tipo de dato: punto flotante. 

### luces__intensidad__baja1_iz

Intensidad de la primera luz baja del lado izquierdo, valor en klux a 1m, con rango entre 0 y 300 de tipo ratio. Tipo de dato: punto flotante. 

### modelo

Año modelo de registro del vehículo, rango comprendido entre 1900 y 2023 de tipo intervalo. Tipo de dato: entero. 

### combustible

Tipo de combustible del vehículo. Tipo de dato: string, valor nominal. Rango: lista de valores. 

### marca

Marca del vehículo. Tipo de dato: string, valor nominal. Rango: lista de valores.

### linea

Línea del vehículo. Tipo de dato: string, valor nominal. Rango: lista de valores. 

### kilometraje

Kilometraje del vehículo (en kilómetros), rango comprendido entre 1 y 10000000, de tipo ratio. El valor 0 indica que el medidor de kilometraje del vehículo no es funcional. Tipo de dato: entero.

### tipo_motor

Tipo de motor para motocicletas: Valor de tipo nominal en variable string, los posibles valores son '2t' o '4t'

### tipo_revision_id

Tipo de revisión que se realiza al vehículo. Tipo de dato: integer, valor nominal.

### codigo_resultado

Resultado de la inspección (rango: 1 => inspección aprobada, 2 => inspección reprobada). Tipo de dato: entero, de tipo nominal. 

### secuencia

Indica el consecutivo de la inspección: 1 si es una inspección de primera vez, 2 si ya había salido rechazado y volvió antes de 15 días sin pagar de nuevo.

### fecha_inicio

Fecha y hora en la que se registra la inspección en el sistema. Tipo de dato: Fecha, intervalo. (rango fecha entre 01/09/2014 – 01/09/2022) (rango hora entre 00:00 y 23:59)

### fecha_fin

Fecha y hora en la que se finaliza la inspección en el sistema. Tipo de dato: Fecha, intervalo. (rango fecha entre 01/09/2014 – 01/09/2022) (rango hora entre 00:00 y 23:59)
