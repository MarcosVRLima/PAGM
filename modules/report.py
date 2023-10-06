import os
import pandas as pd

# Suponha que você tenha seus dados em listas
def report(data):
    xlsxArchive = "report.xlsx"
    # Verifique se o arquivo Excel existe
    if os.path.exists(xlsxArchive):
        # O arquivo existe, abra-o e adicione a nova linha
        df = pd.read_excel(xlsxArchive)
        df = df.append(data, ignore_index=True)
    else:
        # O arquivo não existe, crie um novo DataFrame com a nova linha
        df = pd.DataFrame([data])

    # Salve o DataFrame no arquivo Excel
    df.to_excel(xlsxArchive, index=False)
    print(f'Dados escritos em "{xlsxArchive}"')

