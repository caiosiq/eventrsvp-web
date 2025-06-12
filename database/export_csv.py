import sqlite3
import csv

# Caminho para o banco de dados
DB_PATH = "Pimenta.db"

# Arquivo csv
OUTPUT_FILE = "convidados_export.csv"

def exportar_convidados():
    print("🔄 Iniciando exportação...")
    try:
        # Conecta ao banco SQLite
        conn = sqlite3.connect(DB_PATH)
        print("✅ Conectado ao banco com sucesso.")
        cursor = conn.cursor()

        # Consulta os dados
        cursor.execute("SELECT * FROM convidados")
        rows = cursor.fetchall()

        # Recupera os nomes das colunas
        colunas = [description[0] for description in cursor.description]

        # Escreve no CSV
        with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(colunas)    # cabeçalho
            writer.writerows(rows)  # dados

            print(f"✅ Dados exportados com sucesso para: {OUTPUT_FILE}")

    except Exception as e:
        print(f"❌ Erro ao exportar dados: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    exportar_convidados()