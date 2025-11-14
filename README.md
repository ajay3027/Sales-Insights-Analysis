# Sales Insight Project – README

## 📘 About the Project
The **Sales Insight Project** is a data analysis and visualization solution built using **Power BI**, with supporting **SQL** and **Python** scripts to prepare, load, and refresh the data sources. It is a complete, ready-to-run package so anyone can download, set up, and view the dashboards.

---

## 🎯 Purpose of the Project
- Provide interactive Power BI dashboards for sales analytics.
- Include reproducible data pipelines (Python) and database scripts (SQL) so datasets can be recreated or loaded into a local database.
- Make the project runnable by non-developers with clear step-by-step instructions.

---

## 📥 How to Use This Project (Step-by-Step)
Follow these steps after downloading the project from GitHub.

### **1️⃣ Download or Clone the Project**
- Click **Code → Download ZIP** OR
- Run in terminal:
```
git clone <repo-link>
cd Sales-Insight-Project
```

### **2️⃣ Inspect the Folder Structure**
```
Sales-Insight-Project/
│
├── data_raw/               # Original CSV files (raw input)
├── data_processed/         # Output CSV files created by Python ETL
├── powerbi/                # Power BI (.pbix) dashboard
├── sql/                    # SQL scripts to create/load schema (e.g. create_tables.sql)
├── scripts/                # Python scripts (data processing, load to DB)
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── autopush.bat            # (Optional) Windows script to commit & push
```

### **3️⃣ Option A – Quick run (no DB required)**
If you just want to open the dashboard:
1. Open `powerbi/Sales_Insight_Dashboard.pbix` in Power BI Desktop.
2. If Power BI prompts for data location, point it to the project folder so relative paths resolve.
3. To refresh visuals after changing data, replace CSVs in `data_processed/` (or `data_raw/` if your PBIX points there), then **Home → Refresh**.

### **4️⃣ Option B – Recreate the data pipeline (recommended)**
This runs the Python ETL to clean/transform raw CSVs and optionally load them to a local database.

#### A. Install Python dependencies
(Use Python 3.8+)
```
python -m venv venv
# Windows (from project root, use forward slashes shown)
venv/Scripts/activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

`requirements.txt` should include at least:
```
pandas
sqlalchemy
psycopg2-binary    # if using PostgreSQL
sqlite-utils        # optional helper
python-dotenv       # for environment variables
```

#### B. Run the ETL
```
# cleans raw CSVs and outputs processed CSVs
python scripts/data_processing.py

# optionally load processed CSVs into a DB
python scripts/load_to_db.py --db sqlite:///sales_insight.db
# or for Postgres
python scripts/load_to_db.py --db postgresql://user:pass@localhost:5432/salesdb
```

Notes on scripts provided:
- `data_processing.py` — reads files from `data_raw/`, runs cleaning and joins, writes `data_processed/*.csv`.
- `load_to_db.py` — reads `data_processed/*.csv` and inserts into a specified database using SQLAlchemy.
- `generate_summary.py` (optional) — creates quick summary CSVs used by the PBIX, placed in `data_processed/`.

### **5️⃣ Option C – Use the included SQL scripts**
If you prefer loading the data with SQL:

#### Local SQLite (fast, zero setup)
```
# create DB and load schema
sqlite3 sales_insight.db < sql/create_tables.sql
# load CSVs using sqlite3 (example)
.mode csv
.import data_processed/sales.csv sales
```

#### PostgreSQL (production-like)
1. Create a database and user (example):
```
createdb salesdb
psql -d salesdb -c "CREATE USER analytics WITH PASSWORD 'password';"
psql -d salesdb -c "GRANT ALL PRIVILEGES ON DATABASE salesdb TO analytics;"
```
2. Run schema and import (psql):
```
psql -d salesdb -f sql/create_tables.sql
# Use psql meta-commands or COPY to import CSVs from a server-accessible path
psql -d salesdb -c "COPY sales FROM '/absolute/path/to/data_processed/sales.csv' CSV HEADER;"
```

> Tip: The SQL folder includes `create_tables.sql` and `sample_queries.sql` with useful joins and aggregated queries you can use directly in Power BI (use DirectQuery or import via ODBC).

---

## 🔁 How to point Power BI to processed data
- If you used Python ETL or SQL, make sure `powerbi` file points to the `data_processed/` CSVs or to your database connection.
- To switch a data source in Power BI: **Home → Transform data → Data source settings → Change Source** and provide the new path/connection string.

---

## 🧪 Troubleshooting
- **Missing libraries**: Activate the virtualenv and run `pip install -r requirements.txt`.
- **Power BI can't find CSVs**: Ensure relative paths remain the same (open PBIX from project folder). If necessary update the data source to the folder.
- **DB connection refused**: Check host, port, user, and that the DB server is running.
- **Encoding issues**: CSVs are UTF-8; if you see strange characters, open them with a text editor and confirm encoding.

---

## 🧾 Summary
- This project includes Power BI dashboards, raw and processed CSVs, Python ETL scripts, and SQL schema/import scripts.
- Choose Quick run (open PBIX) or Recreate pipeline (run Python scripts ± SQL load).
- Everything uses relative paths so it’s portable after cloning.

---

## ✅ Next steps I can do for you (pick any):
- Create `requirements.txt` and example Python scripts (`data_processing.py`, `load_to_db.py`).
- Generate `create_tables.sql` and `sample_queries.sql` tailored to your CSV schema.
- Produce a one-page PDF quick-start guide with screenshots.

Tell me which of the above you want me to add and I’ll include them in the repo.

