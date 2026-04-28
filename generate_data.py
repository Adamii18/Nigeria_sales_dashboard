import pandas as pd
import random
import os

# -----------------------------------------------
# DATA SOURCE: National Bureau of Statistics (NBS)
# Report: Selected Food Prices Watch (2024-2025)
# Website: nigerianstat.gov.ng
# Prices are national averages in Nigerian Naira ₦
# -----------------------------------------------

products = {
    # GRAINS & STAPLES
    'Rice Local (1kg)':         1960,   # NBS Nov 2024
    'Rice Foreign (1kg)':       2500,   # NBS estimate 2025
    'White Garri (1kg)':        852,    # NBS Apr 2024
    'Yellow Garri (1kg)':       900,    # NBS Apr 2024
    'Maize Grain (1kg)':        800,    # NBS 2024
    'Wheat Flour (1kg)':        1200,   # NBS 2024

    # PROTEINS
    'Beans Brown (1kg)':        2501,   # NBS Dec 2024
    'Beef Boneless (1kg)':      4712,   # NBS May 2024
    'Frozen Chicken (1kg)':     4829,   # NBS May 2024
    'Catfish (1kg)':            3500,   # NBS 2024
    'Eggs Medium (12 pieces)':  2834,   # NBS Nov 2024
    'Mackerel/Titus (1kg)':     3200,   # NBS 2024

    # VEGETABLES & FRUITS
    'Tomato (1kg)':             1123,   # NBS Apr 2024
    'Onion Bulb (1kg)':         2058,   # NBS Dec 2024
    'Pepper (1kg)':             2000,   # NBS 2024
    'Yam Tuber (1kg)':          1130,   # NBS Apr 2024
    'Sweet Potato (1kg)':       800,    # NBS 2024
    'Plantain (1kg)':           900,    # NBS 2024
    'Spinach/Ugu (bunch)':      500,    # NBS 2024

    # OILS & CONDIMENTS
    'Palm Oil (1 litre)':       2500,   # NBS 2024
    'Vegetable Oil (5 litres)': 20000,  # NBS 2025
    'Groundnut Oil (1 litre)':  3000,   # NBS 2024
    'Salt (1kg)':               600,    # NBS 2024
    'Tomato Paste (small tin)': 500,    # NBS 2024

    # DRINKS & OTHERS
    'Water (75cl bottle)':      300,    # NBS 2024
    'Soft Drink (50cl bottle)': 500,    # NBS 2024
}

categories = {
    'Rice Local (1kg)':         'Grains',
    'Rice Foreign (1kg)':       'Grains',
    'White Garri (1kg)':        'Grains',
    'Yellow Garri (1kg)':       'Grains',
    'Maize Grain (1kg)':        'Grains',
    'Wheat Flour (1kg)':        'Grains',
    'Beans Brown (1kg)':        'Proteins',
    'Beef Boneless (1kg)':      'Proteins',
    'Frozen Chicken (1kg)':     'Proteins',
    'Catfish (1kg)':            'Proteins',
    'Eggs Medium (12 pieces)':  'Proteins',
    'Mackerel/Titus (1kg)':     'Proteins',
    'Tomato (1kg)':             'Vegetables',
    'Onion Bulb (1kg)':         'Vegetables',
    'Pepper (1kg)':             'Vegetables',
    'Yam Tuber (1kg)':          'Vegetables',
    'Sweet Potato (1kg)':       'Vegetables',
    'Plantain (1kg)':           'Vegetables',
    'Spinach/Ugu (bunch)':      'Vegetables',
    'Palm Oil (1 litre)':       'Oils',
    'Vegetable Oil (5 litres)': 'Oils',
    'Groundnut Oil (1 litre)':  'Oils',
    'Salt (1kg)':               'Condiments',
    'Tomato Paste (small tin)': 'Condiments',
    'Water (75cl bottle)':      'Drinks',
    'Soft Drink (50cl bottle)': 'Drinks',
}

# Generate 1000 sales records
random.seed(42)
records = []

months = list(range(1, 13))
month_names = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']

for _ in range(1000):
    product = random.choice(list(products.keys()))
    price = products[product]
    quantity = random.randint(1, 30)
    month = random.choice(months)
    # Simulate higher sales in festive months
    if month in [12, 1, 4]:
        quantity = int(quantity * 1.5)
    revenue = price * quantity
    records.append({
        'Month': month,
        'Month_Name': month_names[month - 1],
        'Product': product,
        'Category': categories[product],
        'Unit_Price': price,
        'Quantity': quantity,
        'Revenue': revenue
    })

df = pd.DataFrame(records)
df = df.sort_values('Month').reset_index(drop=True)

# Save
output_path = "/storage/emulated/0/Lesson/sales-dashboard/data/sales_data.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("✅ Sales data generated successfully!")
print(f"Total records: {len(df)}")
print(f"Total Revenue: ₦{df['Revenue'].sum():,.0f}")
print(f"Total Products: {df['Product'].nunique()}")
print(f"Categories: {df['Category'].unique().tolist()}")
print(f"\nSample:\n{df.head()}")