# Eriri - base

## Description

This project performs import, comparison, and export of data between CSV files and a MySQL database. It loads data from two files, stores them in separate tables, compares the records, and exports the differences to a new CSV file.

## Features

- Cleans database tables.
- Imports data from CSV files into MySQL.
- Compares two tables to identify differences.
- Exports differing records to a `new_data.csv` file.
- Parallel processing for better performance.

## How to Use

1. **Prerequisites**  
   - Python 3.x  
   - MySQL  
   - `pymysql` library  
   - Data files: `data.txt` (tab-delimited) and `data2.txt` (semicolon-delimited)

2. **Install dependencies**  
   ```bash
   pip install pymysql
   ```

3. **Database setup**  
   Make sure the `primary_base` database and the tables `primary_sheet` and `secondary_sheet` exist.

4. **Execution**  
   ```bash
   python script.py
   ```
   The script will ask if you want to clear the tables before importing data.

5. **Output**  
   - The result with the differences will be saved in `new_data.csv`.

## Data file structure

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

## Notes

- Edit the `format_name` function in `script.py` to apply name normalization rules if needed.
- Adjust the database credentials according to your environment.

---