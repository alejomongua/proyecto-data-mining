import pandas as pd

CAMPOS_GASES = [
    'gases__ralenti__co',
    'gases__ralenti__co2',
    'gases__ralenti__hc',
    'gases__ralenti__o2',
    'modelo',
    'marca',
    'linea',
    'kilometraje',
    'codigo_resultado',
    'secuencia',
    'fecha_fin',
]

def eliminar_duplicados(dataframe, campos_ignorados):
    """Se eliminan los registros duplicados"""
    # No se tienen en cuenta algunos campos
    columnas_para_duplicados = list(dataframe.columns)
    for campo in campos_ignorados:
        columnas_para_duplicados.remove(campo)

    dataframe.drop_duplicates(inplace=True, subset=columnas_para_duplicados)

def eliminar_valores_incoherentes(dataframe, campos):
    """
    Se eliminan los valores que, desde el conocimiento de los datos
    se sabe que corresponden a errores en la lectura del dato o en la
    digitación

    Esta función recibe como parámetros el dataframe y un diccionario
    de campos donde cada llave tiene asociado un array de longitud 2
    donde se almacena el límite inferior y el límite superior respectivamente
    de los valores que se consideran coherentes
    """
    for campo in campos:
        niveles = campos[campo]
        lim_inferior = niveles[0]
        lim_superior = niveles[1]

        dataframe = dataframe[(dataframe[campo] > lim_inferior) & (dataframe[campo] < lim_superior)]
    
    return dataframe

def main():
    """Punto de entrada"""
    # Cargo el dataset
    df = pd.read_hdf('datos/dataframe.hdf')

    # Extraigo los datos con los que voy a trabajar:
    # tipo de revisión 1 que corresponde a automóviles livianos
    # Combustible gasolina
    # Extraigo solo las columnas que me interesa
    carros_df = df[(df['tipo_revision_id'] == 1) & (df['combustible'] == 'GASOLINA')][CAMPOS_GASES]

    # En las columnas de interes, eliminamos los registros con valores faltantes
    carros_df.dropna(how='any', inplace=True)

    # Eliminamos los valores duplicados
    eliminar_duplicados(carros_df, ['kilometraje', 'codigo_resultado', 'secuencia', 'CDA'])

    # Elimina valores incoherentes
    carros_df = eliminar_valores_incoherentes(carros_df, {
        'gases__ralenti__co': [-0.5, 25],
        'gases__ralenti__co2': [-0.5, 25],
        'gases__ralenti__hc': [-0.5, 2**16],
        'gases__ralenti__o2': [-0.5, 25],
        # Los carros inspeccionados son carros usados, por lo tanto no
        # tienen sentido kilometrajes demasiado bajos:
        'kilometraje': [101, 10**6], 
    })

    # Se crea un atributo "artificial" llamado antiguedad para almacenar
    # la edad del vehículo en el momento de la prueba
    carros_df['antiguedad'] = carros_df['fecha_fin'].map(lambda x: x.year) * carros_df['modelo']
    
    # Se eliminan las dos columnas ahora innecesarias: fecha_fin y modelo
    carros_df.drop(['modelo', 'fecha_fin'], axis=1, inplace=True)

    # Se saca una muestra para calcular los promedios
    sample_df = carros_df.sample(10000)

    mean = sample_df.mean()
    stdev = sample_df.stdev()

if __name__ == '__main__':
    main()