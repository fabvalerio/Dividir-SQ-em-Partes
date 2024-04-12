import os

def group_sql_files():
    # Pedir ao usuário que especifique os diretórios de entrada e saída e o tamanho máximo
    input_dir = input('Por favor, informe o diretório de entrada (onde estão os arquivos SQL divididos): ')
    output_dir = input('Por favor, informe o diretório de saída (onde os arquivos agrupados serão salvos): ')
    max_size_mb = float(input('Por favor, informe o tamanho máximo para cada arquivo de saída em MB: '))

    # Verificar e criar o diretório de saída, se necessário
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = [f for f in os.listdir(input_dir) if f.endswith('.sql')]
    files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))  # Ordena os arquivos por número

    group_num = 1
    current_size = 0
    grouped_content = ""

    for filename in files:
        file_path = os.path.join(input_dir, filename)
        # Obter o tamanho do arquivo em MB
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        
        # Verificar se adicionar este arquivo excederia o limite de tamanho
        if current_size + file_size_mb > max_size_mb:
            # Salvar o grupo atual antes de exceder o limite
            output_file_path = os.path.join(output_dir, f'group_{group_num}.sql')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(grouped_content)
            group_num += 1
            current_size = 0
            grouped_content = ""
        
        # Adicionar o conteúdo do arquivo atual ao grupo
        with open(file_path, 'r', encoding='utf-8') as input_file:
            grouped_content += input_file.read()
        current_size += file_size_mb

    # Não esquecer de salvar o último grupo se ele contiver algum arquivo
    if grouped_content:
        output_file_path = os.path.join(output_dir, f'group_{group_num}.sql')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(grouped_content)

# Executar a função com a interação do usuário
group_sql_files()
