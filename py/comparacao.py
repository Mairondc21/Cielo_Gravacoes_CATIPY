import os
import filecmp

def compare_files_in_subfolders(dir1, dir2):
    # Dicionário para armazenar os arquivos de cada diretório
    files_dir1 = {}
    files_dir2 = {}
    
    # Função para percorrer as subpastas e armazenar os arquivos
    def walk_directory(directory, files_dict):
        for root, _, files in os.walk(directory):
            for file in files:
                # Armazenar o caminho relativo do arquivo para comparar as subpastas
                nome_tratado = file[0:9]
                rel_path = os.path.relpath(os.path.join(root, nome_tratado), directory)
                files_dict[rel_path] = os.path.join(root, nome_tratado)
    
    # Percorrer as subpastas e armazenar os arquivos
    walk_directory(dir1, files_dir1)
    walk_directory(dir2, files_dir2)
    
    # Comparar os arquivos entre as subpastas correspondentes
    common_files = set(files_dir1.keys()).intersection(files_dir2.keys())
    only_in_dir1 = set(files_dir1.keys()) - set(files_dir2.keys())
    only_in_dir2 = set(files_dir2.keys()) - set(files_dir1.keys())
    
    print("Arquivos encontrados em ambas as pastas e que serão comparados:")
    for file in common_files:
        file1 = files_dir1[file]
        file2 = files_dir2[file]
        if filecmp.cmp(file1, file2, shallow=False):
            print(f"{file} é idêntico em ambos os diretórios.")
        else:
            print(f"{file} é diferente em ambos os diretórios.")
    
    print("\nArquivos presentes apenas no primeiro diretório:")
    for file in only_in_dir1:
        print(file)
    
    print("\nArquivos presentes apenas no segundo diretório:")
    for file in only_in_dir2:
        print(file)

# Exemplo de uso:
caminho1 = r'C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\Audio_Cortes\Cadu'
caminho2 = r'C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\Audio_Cortes\Cadu_00\Output\2024-08-28'

compare_files_in_subfolders(caminho1, caminho2)
