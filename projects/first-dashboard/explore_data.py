import csv
from collections import Counter

with open("combined_csp_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total rows: {len(rows)}")
print(f"\nColumns: {list(rows[0].keys())}")

products = Counter(r["Product Title"] for r in rows if r["Product Title"])
print(f"\nProducts ({len(products)}):")
for p, c in products.most_common(10):
    print(f"  {c:>5}  {p}")

providers = Counter(r["Cloud Provider"] for r in rows if r["Cloud Provider"])
print(f"\nCloud Providers:")
for p, c in providers.most_common():
    print(f"  {c:>5}  {p}")

countries = Counter(r["Country"] for r in rows if r["Country"])
print(f"\nTop 10 Countries:")
for p, c in countries.most_common(10):
    print(f"  {c:>5}  {p}")

dates = sorted(set(r["Usage Date"] for r in rows if r["Usage Date"] and r["Product Title"]))
print(f"\nDate range: {dates[0]} to {dates[-1]}")
print(f"Unique dates: {len(dates)}")

companies = Counter(r["Company Name"] for r in rows if r["Company Name"])
print(f"\nTotal unique companies: {len(companies)}")
print("Top 10 Companies:")
for p, c in companies.most_common(10):
    print(f"  {c:>5}  {p}")
