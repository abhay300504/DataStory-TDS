# Create project files for the Manufacturing Performance Analysis PR
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import dedent
import zipfile, os

# 1) Create data.csv
data_csv = dedent("""
quarter,efficiency
Q1,73.84
Q2,74.35
Q3,77.48
Q4,80.25
""").strip() + "\n"

with open("data.csv", "w") as f:
    f.write(data_csv)

# 2) Create analysis.py (reads CSV, computes stats, prints, and plots trend vs target 90)
analysis_py = dedent(f"""
# Manufacturing Performance Analysis
# Email (verification): 23f1001119@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

TARGET = 90.0

def main():
    df = pd.read_csv("data.csv")
    # Ensure order Q1..Q4
    order = ["Q1","Q2","Q3","Q4"]
    df["quarter"] = pd.Categorical(df["quarter"], categories=order, ordered=True)
    df = df.sort_values("quarter")
    
    avg = round(df["efficiency"].mean(), 2)
    print(f"Average equipment efficiency: {{avg}}")
    
    # Simple trend plot vs target
    plt.figure(figsize=(8, 5))
    plt.plot(df["quarter"], df["efficiency"], marker="o", label="Equipment Efficiency")
    plt.axhline(TARGET, linestyle="--", label="Industry Target (90)")
    plt.title("Equipment Efficiency Rate — 2024 Quarterly Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Efficiency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("trend_vs_target.png")
    print("Saved chart: trend_vs_target.png")

if __name__ == "__main__":
    main()
""").strip()

with open("data.csv", "w") as f:
    f.write(analysis_py)

# 3) Create README.md with data story, findings, business implications, and recommendations
from textwrap import dedent

# Create the README content
readme_md = dedent("""\
# Manufacturing Performance Analysis (2024)
**Email (verification): 23f1001119@ds.study.iitm.ac.in**

This Pull Request analyzes quarterly **Equipment Efficiency Rate** for 2024, compares it to the **industry target (90)**, and recommends actions to close the gap via a **predictive maintenance program**.

## Dataset
- Q1: 73.84  
- Q2: 74.35  
- Q3: 77.48  
- Q4: 80.25  

**Average (must be correct): 76.48**

Data is stored in `data.csv`.

## How to run
```bash
python analysis.py
""")

with open("README.md", "w") as f:
    f.write(readme_md)