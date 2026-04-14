import pandas as pd
import matplotlib.pyplot as plt

# Source data
data = {
    "Month": [
        "Jan-24","Feb-24","Mar-24","Apr-24","May-24","Jun-24",
        "Jul-24","Aug-24","Sep-24","Oct-24","Nov-24","Dec-24",
        "Jan-25","Feb-25","Mar-25","Apr-25","May-25","Jun-25"
    ],
    "DSO": [44.0,45.0,46.0,45.0,44.0,43.0,45.0,46.0,47.0,48.0,47.0,45.0,46.0,48.0,49.0,51.0,51.0,52.0],
    "DIO": [28.0,27.0,28.0,29.0,28.0,28.0,30.0,30.0,31.0,32.0,31.0,29.0,31.0,32.0,33.0,33.0,34.0,34.0],
    "DPO": [30.0,30.0,31.0,31.0,30.0,30.0,31.0,32.0,32.0,33.0,33.0,31.0,33.0,34.0,34.0,35.0,36.0,38.0],
}

df = pd.DataFrame(data)
df["Month"] = pd.to_datetime(df["Month"], format="%b-%y")
df = df.sort_values("Month")

# Calculated measure
df["CCC"] = df["DSO"] + df["DIO"] - df["DPO"]

# Component movement summary
movement = {
    "DSO": df["DSO"].iloc[-1] - df["DSO"].iloc[0],
    "DIO": df["DIO"].iloc[-1] - df["DIO"].iloc[0],
    "DPO": df["DPO"].iloc[-1] - df["DPO"].iloc[0],
    "CCC": df["CCC"].iloc[-1] - df["CCC"].iloc[0],
}
print("Net movement (end vs start):", movement)

# -------- Option 1: Multi-series line chart --------
plt.figure(figsize=(12, 6))
plt.plot(df["Month"], df["CCC"], marker="o", linewidth=2.5, label="CCC (days)")
plt.plot(df["Month"], df["DSO"], marker="o", linestyle="--", label="DSO (days)")
plt.plot(df["Month"], df["DIO"], marker="o", linestyle="--", label="DIO (days)")
plt.plot(df["Month"], df["DPO"], marker="o", linestyle="--", label="DPO (days)")

plt.title("Cash Conversion Cycle and Components by Month")
plt.xlabel("Month")
plt.ylabel("Days")
plt.xticks(df["Month"], [d.strftime("%b-%y") for d in df["Month"]], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -------- Option 2: Combo chart --------
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(df["Month"], df["CCC"], width=20, label="CCC (days)", alpha=0.6)
ax1.set_xlabel("Month")
ax1.set_ylabel("CCC (days)")
ax1.set_title("Cash Conversion Cycle with DSO, DIO, and DPO Components")
ax1.set_xticks(df["Month"])
ax1.set_xticklabels([d.strftime("%b-%y") for d in df["Month"]], rotation=45)

ax2 = ax1.twinx()
ax2.plot(df["Month"], df["DSO"], marker="o", linestyle="--", label="DSO (days)")
ax2.plot(df["Month"], df["DIO"], marker="o", linestyle="--", label="DIO (days)")
ax2.plot(df["Month"], df["DPO"], marker="o", linestyle="--", label="DPO (days)")
ax2.set_ylabel("Component days")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.tight_layout()
plt.show()