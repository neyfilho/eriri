# Eriri

## Descrição

Este projeto realiza a importação, comparação e exportação de dados entre arquivos CSV e um banco de dados MySQL. Ele carrega dados de dois arquivos, armazena em tabelas distintas, compara os registros e exporta as divergências para um novo arquivo CSV.

## Funcionalidades

- Limpeza das tabelas do banco de dados.
- Importação de dados de arquivos CSV para o MySQL.
- Comparação entre duas tabelas para identificar divergências.
- Exportação dos dados divergentes para um arquivo `new_data.csv`.
- Processamento paralelo para maior desempenho.

## Como usar

1. **Pré-requisitos**  
   - Python 3.x  
   - MySQL  
   - Biblioteca `pymysql`  
   - Arquivos de dados: `data.txt` (delimitado por tabulação) e `data2.txt` (delimitado por ponto e vírgula)

2. **Instalação das dependências**  
   ```bash
   pip install pymysql
   ```

3. **Configuração do banco de dados**  
   Certifique-se de que o banco `primary_base` e as tabelas `primary_sheet` e `secondary_sheet` existem.

4. **Execução**  
   ```bash
   python script.py
   ```
   O script perguntará se deseja limpar as tabelas antes de importar os dados.

5. **Saída**  
   - O resultado das divergências será salvo em `new_data.csv`.

## Estrutura dos arquivos de dados

- `data.txt`:  
  ```
  id<TAB>name
  1<TAB>João
  2<TAB>Maria
  ```
- `data2.txt`:  
  ```
  id;name
  1;João
  2;Mariana
  ```

## Observações

- Edite a função `format_name` em `script.py` para aplicar regras de normalização de nomes, se necessário.
- Ajuste as credenciais do banco de dados conforme seu ambiente.

---