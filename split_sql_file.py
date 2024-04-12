import re
import os

def split_sql_file(input_file):
    # Pedir ao usuário que especifique o diretório de saída
    output_dir = input('Por favor, informe o diretório de saída onde os arquivos divididos serão salvos: ')

    # Verifica se o diretório de saída existe, se não, cria o diretório
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_count = 1
    output_content = ""

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if re.match(r'^INSERT INTO', line):
                if output_content:  # Se existir conteúdo para salvar
                    output_path = os.path.join(output_dir, f'part_{file_count}.sql')
                    with open(output_path, 'w', encoding='utf-8') as out_file:
                        out_file.write(output_content)
                        file_count += 1
                        output_content = ""
            output_content += line

        # Salvar o último pedaço após sair do loop
        if output_content:
            output_path = os.path.join(output_dir, f'part_{file_count}.sql')
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(output_content)

# Pedir ao usuário para informar o caminho do arquivo de entrada
input_file = input('Por favor, informe o caminho completo para o arquivo SQL que deseja dividir: ')
split_sql_file(input_file)
