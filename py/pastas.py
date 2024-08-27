import os

def renomear_arquivos_mp3(caminho_pasta):
    # Lista as subpastas dentro da pasta principal
    subpastas = [f.name for f in os.scandir(caminho_pasta) if f.is_dir()]
    
    for subpasta in subpastas:
        caminho_subpasta = os.path.join(caminho_pasta, subpasta)
        
        # Lista os arquivos dentro da subpasta
        arquivos = os.listdir(caminho_subpasta)
        
        for arquivo in arquivos:
            caminho_subarquivos = os.path.join(caminho_subpasta,arquivo)

            subarquivos = os.listdir(caminho_subarquivos)

            for subarquivo in subarquivos:
                if subarquivo.endswith('.mp3'):
                    caminho_arquivo_antigo = os.path.join(caminho_subarquivos, subarquivo)
                    
                    
                    nome_completo = os.path.basename(caminho_arquivo_antigo)
                    nome = os.path.splitext(nome_completo)[0]
                    extensao = os.path.splitext(nome_completo)[1]
                    
                    # Cria o novo nome de arquivo, adicionando o nome da subpasta antes da extensão
                    novo_nome_arquivo = f"{nome}{arquivo}{extensao}"
                    caminho_arquivo_novo = os.path.join(caminho_subpasta, novo_nome_arquivo)
                    
                    # Renomeia o arquivo
                    os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)
                    print(f"Arquivo renomeado de {arquivo} para {novo_nome_arquivo}")

caminho_da_pasta_principal = r'C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\Audio_Cortes\Rayner\2024.08.26'
renomear_arquivos_mp3(caminho_da_pasta_principal)                