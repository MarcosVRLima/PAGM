import os

def listar_arquivos_em_pasta(caminho_da_pasta):
    nomes_de_arquivos = []
    
    # Verifica se o caminho é um diretório válido
    if os.path.isdir(caminho_da_pasta):
        # Percorre todos os arquivos na pasta e suas subpastas
        for pasta_raiz, subpastas, arquivos in os.walk(caminho_da_pasta):
            for nome_de_arquivo in arquivos:
                nomes_de_arquivos.append(os.path.join(pasta_raiz, nome_de_arquivo).replace("\\", "/"))
    else:
        print(f"nao existe")

    return nomes_de_arquivos

# Substitua 'caminho_da_pasta' pelo caminho da pasta que você deseja listar
# caminho_da_pasta = './AGM/'
# nomes_de_arquivos = listar_arquivos_em_pasta(caminho_da_pasta)

# for nome in nomes_de_arquivos:
#     print(nome)
