def datasetForGraph(df, seriesColor=None, seriesFill='false'):
    '''
    df tem 2 colunas: x e y
    '''

    dataSeriesTemplate = '''
    {
          label: '{seriesName}',
          data: {seriesValues},
          borderColor: '{seriesColor}',
          fill: {seriesFill}
        }
    '''

    