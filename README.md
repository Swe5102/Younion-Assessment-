# Mini Data App Project 

<p align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" width="40" height="40" alt="SQL Server"/> 
<img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" width="40" alt="SSMS"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="40" height="40" alt="VS Code"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" alt="Python"/> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="40" height="40" alt="Pandas"/>  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="40" height="40" alt="NumPy"/> 
<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="40" height="40" alt="Streamlit"/>
</p>


---

## 1. Step‑by‑Step approach for running the project

This section explains the complete execution flow starting from dataset upload to viewing the UI dashboard.

---

### 🔶 Upload Datasets into SQL Server

1. Open **SQL Server Management Studio (SSMS)**
2. Upload the files in the database

   * `leads.csv` → table name: `leads`
   * `campaign_touches.csv` → table name: `campaign_touches`
   * `sales_activity.csv` → table name: `sales_activity`

Note: Use *Import Flat File Wizard* or _Import Data_

---

### 🔶 Run the SQL Unification Query

1. Open a new query window in SSMS
2. Paste the provided **unification SQL query**
3. Execute the query to generate the unified result
4. Save the output as a table (example: `unified_view`)


```sql
SELECT ... INTO unified_view FROM ...
```

This table represents the **final deduplicated unified dataset**


<img width="600" height="750" alt="s1" src="https://github.com/user-attachments/assets/e45a5016-dd74-4263-89ac-9397f060e6d3" />

---

### 🔶 Export the Unified Table

1. Right‑click on `unified_view` table
2. Export the table as a CSV file
3. Save the file locally (example):

```
C:/project/data/unified_view.csv
```

### 🔶 Install the required packages for Filter UI 

1. Install VS code (_It is preferred_)
2. Use the code `Code_for_UI` given in repository 
3. Open New terminal / command prompt and run:

```bash
pip install streamlit
```
<img width="600" height="750" alt="Screenshot 2026-02-03 073744" src="https://github.com/user-attachments/assets/0e00803d-6b81-4dc4-80f8-4bd9fdbc697e" />

---
---

### 🔶 Update File Path in UI Code

1. Open the Streamlit UI Python file
2. Update the file path to point to the exported CSV:

```python
file_path = "C:/project/data/unified_view.csv"
```

Ensure the path matches the saved CSV location.

---
### 🔶 Verify the Streamlit Installation

Run the test command:

```bash
streamlit hello
```
<img width="600" height="750" alt="Screenshot 2026-02-03 073930" src="https://github.com/user-attachments/assets/c0c66d91-0e0b-464f-a27f-94f7591209bc" />



If the demo app opens, Streamlit is installed correctly.



<img width="600" height="750" alt="Screenshot 2026-02-03 074017" src="https://github.com/user-attachments/assets/8f69904d-80a4-4c75-af87-ccd1137e4139" />

---

### 🔶 Save and Run the UI Application

1. Save the UI code as a Python file (example):

```
app.py
```

2. Run the application:

```bash
streamlit run app.py
```
<img width="600" height="750" alt="Screenshot 2026-02-03 074237" src="https://github.com/user-attachments/assets/d307df3c-bd27-4bb8-95fa-27dd2fe17318" />

---

### 🔶 Access the Dashboard

1. Browser opens automatically
2. URL displayed:

```
http://localhost:8501
```
<img width="600" height="750" alt="s3" src="https://github.com/user-attachments/assets/cf80aba8-082a-442a-b366-568f97f585aa" />

---

### 🔶 Use the Filters in the UI

1. Unified rows are shown on initial load
2. Filters dynamically update the table
  

<img width="600" height="750" alt="s4" src="https://github.com/user-attachments/assets/a1c27d24-2122-471d-bbb3-a1f8efc39d9f" />

---

## 2. Data Generation Approach

The datasets were generated using **Breadcrumb AI** through structured prompts to simulate realistic CRM behavior.

* Duplicate and missing emails across datasets
* Inconsistent Company spellings
* Varied date format 

---

## 3. Unification Rules

* Email used as the primary join key
* LEFT JOINs used to retain all leads
* One output row per lead

---

## 4. Deduplication Logic

* GROUP BY applied on lead‑level fields
* Aggregations used to collapse multiple records into a single row per lead


---

## 5. Assumptions

* Email uniquely identifies a lead
* Stage ordering is approximated
* Synthetic data reflects real CRM structure

---

## 6. Limitations

* Stage selection is not fully time‑aware
* Owner assignment may not represent latest change
* Unified ID is for presentation only

---



