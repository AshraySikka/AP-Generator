# AP-Generator
# 📈 Arithmetic Progression (AP) Series Generator

This Python program prints an **Arithmetic Progression (AP)** series based on user-provided inputs.

---

## 📌 What It Does

- Accepts:
  - The first term of the series
  - The common difference
  - The number of terms to print
- Generates and displays the AP series.

---

## 🧠 How It Works

1. Takes the **first term** `a`, **common difference** `d`, and **number of terms** `n` as input from the user.
2. Uses a `for` loop with Python's `range()` to generate each term:
   - Formula used:  
     **nth term = a + (n - 1) × d**
   - Loop:  
     `range(a, (a + (n-1)*d) + 1, d)`

---

## ▶️ Sample Output

Enter the first term of the series: 2
Enter the common difference of the series: 3
Enter the number of terms you want to print: 5
2
5
8
11
14


---

## 📋 Formula Recap

**Arithmetic Progression** is defined by:
- First term: `a`
- Common difference: `d`
- Number of terms: `n`
- nth term: `a + (n - 1) * d`

---

## 🚀 How to Run

Save the code as `ap-series.py` and run it:

```bash
python ap-series.py
