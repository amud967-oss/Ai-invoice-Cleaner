import pandas as pd

data = [
    {"date": " 22 May 2026 ", "amount": " ₦10,000.00 ", "status": "Success "},
    {"date": "23 May 2026", "amount": "N5,000", "status": " success"},
    {"date": "  ", "amount": "10000", "status": "FAILED"},
]

df = pd.DataFrame(data)
print("MESSY DATA:")
print(df)

df['date'] = df['date'].str.strip()
df['amount'] = df['amount'].str.replace('₦', '').str.replace('N', '').str.replace(',', '').str.strip()
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df['status'] = df['status'].str.strip().str.lower()

print("\nCLEAN DATA:")
print(df)

df.to_excel("clean_receipts.xlsx", index=False)
print("\nExcel created! clean_receipts.xlsx")