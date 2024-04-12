


<img src="logo.png">


# Dividir-SQL (DADOS)-em-Partes via Python

O script `split_sql_file.py` é projetado para dividir um arquivo SQL grande em partes menores com base em instruções de inserção (`INSERT INTO`). Aqui está um resumo de como ele funciona:

1. Solicita ao usuário que especifique o diretório de saída onde os arquivos divididos serão salvos.
2. Verifica se o diretório de saída existe. Se não existir, o script cria o diretório.
3. Abre o arquivo SQL de entrada e lê seu conteúdo linha por linha.
4. Sempre que encontra uma linha que começa com `INSERT INTO`, o script considera que é o início de um novo bloco de dados.
   * Se já houver conteúdo acumulado para ser salvo, ele salva esse conteúdo em um novo arquivo no diretório de saída, e então reinicia a acumulação de conteúdo para o próximo arquivo.
5. Cada novo arquivo criado é nomeado como `part_{número}.sql`, com `{número}` incrementado para cada novo arquivo.
6. O processo continua até que todas as linhas do arquivo de entrada tenham sido processadas.
7. Se houver conteúdo que ainda não foi salvo ao final do arquivo, este é salvo em um último arquivo de saída.

Agora, vamos analisar o segundo script, `group_sql_files.py`, para entender como ele agrupa os arquivos divididos anteriormente, considerando um tamanho desejado em MB, possivelmente para se adequar à restrição de tamanho de upload do phpMyAdmin. 

O script `group_sql_files.py` é projetado para agrupar arquivos SQL divididos em arquivos maiores, dentro de um limite de tamanho especificado pelo usuário (em MB), o que pode ser útil para contornar limitações de upload como as encontradas no phpMyAdmin. Aqui está um resumo de como ele funciona:

1. Solicita ao usuário que especifique o diretório de entrada (onde estão os arquivos SQL divididos), o diretório de saída (onde os arquivos agrupados serão salvos) e o tamanho máximo para cada arquivo de saída em MB.
2. Verifica se o diretório de saída existe. Se não, o cria.
3. Lista e ordena os arquivos `.sql` presentes no diretório de entrada.
4. Itera sobre os arquivos, agregando o conteúdo de cada um a um "arquivo agrupado" enquanto o tamanho total do grupo não exceder o limite especificado pelo usuário.
5. Se o adicionar o conteúdo de um arquivo ao grupo atual fizer com que o tamanho exceda o limite:
   * O conteúdo acumulado é salvo em um novo arquivo no diretório de saída, e o processo de acumulação é reiniciado para o próximo arquivo agrupado.
6. Cada novo arquivo agrupado é nomeado como `group_{número}.sql`, com `{número}` incrementado para cada novo arquivo.
7. O processo continua até que todos os arquivos de entrada tenham sido processados.
8. Se houver conteúdo que ainda não foi salvo ao final da iteração, este é salvo em um último arquivo agrupado.

Com base na funcionalidade descrita dos scripts `split_sql_file.py` e `group_sql_files.py`, podemos compilar um manual de uso em etapas. Vou fazer isso a seguir. 


# Manual de Uso para Divisão e Agrupamento de Arquivos SQL

Este manual descreve como dividir um grande arquivo SQL em partes menores e, posteriormente, como agrupar essas partes em arquivos de tamanho específico. Este processo pode ser útil para contornar limitações de upload de arquivos, como o limite de `max_upload_size` do phpMyAdmin.

### Divisão de Arquivo SQL

1. **Preparação** : Certifique-se de que o arquivo SQL que deseja dividir esteja acessível e você saiba o caminho até ele.
2. **Execução do Script de Divisão** :

* Execute o script, informe o caminho completo do arquivo SQL que deseja dividir e o diretório
  ```
  python .\split_sql_file.py dir\arquivo.sql dir\saida
  ```
* Se o diretório não existir, ele será criado.

1. **Verificação** : Navegue até o diretório de saída especificado. Você encontrará vários arquivos nomeados como `part_{número}.sql`, representando partes do arquivo original.

### Agrupamento de Arquivos SQL Divididos

1. **Preparação** : Tenha em mãos o diretório contendo os arquivos SQL divididos e decida sobre o tamanho máximo em MB para cada arquivo agrupado.
2. **Execução do Script de Agrupamento** :

* Execute o script
  ```
  python .\group_sql_files.py
  ```
* Quando solicitado, informe o diretório de entrada (onde estão os arquivos SQL divididos).
* Informe o diretório de saída onde os arquivos agrupados serão salvos. Se o diretório não existir, ele será criado.
* Informe o tamanho máximo em MB para cada arquivo de saída. Este valor deve levar em conta as limitações de upload que você deseja contornar.

1. **Verificação** : Navegue até o diretório de saída especificado. Você encontrará arquivos nomeados como `group_{número}.sql`, cada um contendo o conteúdo agrupado dos arquivos divididos e respeitando o limite de tamanho especificado.

### Observações Importantes

* O processo de divisão é baseado na presença de instruções `INSERT INTO`, iniciando um novo arquivo dividido a cada ocorrência.
* O processo de agrupamento respeita um limite de tamanho específico, garantindo que cada arquivo agrupado não exceda o tamanho máximo definido.
* Ambos os scripts interagem com o usuário através do terminal, solicitando informações necessárias para a execução.

Este manual destina-se a facilitar o gerenciamento de grandes arquivos SQL, especialmente em situações com restrições de tamanho de arquivo para uploads.
