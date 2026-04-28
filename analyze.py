import pandas as pd

# Load data
file_path = "/storage/emulated/0/Lesson/sales-dashboard/data/sales_data.csv"
df = pd.read_csv(file_path)

print("=== TOTAL REVENUE ===")
print(f"₦{df['Revenue'].sum():,.0f}")

print("\n=== REVENUE BY CATEGORY ===")
cat = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
for c, v in cat.items():
    print(f"{c}: ₦{v:,.0f}")

print("\n=== TOP 5 BEST SELLING PRODUCTS ===")
top = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)
for p, v in top.items():
    print(f"{p}: ₦{v:,.0f}")

print("\n=== MONTHLY REVENUE ===")
monthly = df.groupby('Month_Name')['Revenue'].sum()
month_order = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']
monthly = monthly.reindex(month_order)
for m, v in monthly.items():
    print(f"{m}: ₦{v:,.0f}")

print("\n=== BEST MONTH ===")
best = monthly.idxmax()
print(f"{best}: ₦{monthly.max():,.0f}")

print("\n=== WORST MONTH ===")
worst = monthly.idxmin()
print(f"{worst}: ₦{monthly.min():,.0f}")