# 🏗️ Flexural Design of Steel Beams — IS 800:2007 (Python Implementation)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Code Standard](https://img.shields.io/badge/Standard-IS%20800%3A2007-orange)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](#)

This Python project performs **flexural, shear, and deflection checks** for a steel beam as per the **Indian Standard IS 800:2007 (General Construction in Steel – Code of Practice)**.  
It reads input parameters from a text file, computes design capacities, checks safety criteria, and outputs results to an output file.

---

## 📘 Features

✅ Calculates **moment capacity (Md)** and compares with the applied moment (M).  
✅ Calculates **shear capacity (Vd)** and compares with the applied shear (V).  
✅ Checks **deflection safety** against permissible limits (L/300).  
✅ Generates a detailed report with safety verdicts and recommendations.  
✅ Fully automated — reads from `input.txt`, writes to `output.txt`.

---

## 📂 Project Structure

```
├── flexural_design.py   # Main Python script
├── input.txt            # Input data file
├── output.txt           # Generated results file (after execution)
└── README.md            # Documentation
```

---

## 🧮 Input Format (`input.txt`)

Each line of the file contains one parameter, in this exact order:

| Line | Parameter | Description | Unit |
|------|------------|-------------|------|
| 1 | V | Applied Shear Force | kN |
| 2 | M | Applied Moment | kNm |
| 3 | L | Effective Span | mm |
| 4 | Ze | Section Modulus | mm³ |
| 5 | fy | Yield Stress | MPa |
| 6 | γₘ₀ | Partial Safety Factor (Material) | — |
| 7 | β_b | Bending Coefficient | — |
| 8 | A_v | Shear Area | mm² |
| 9 | τ_v | Shear Coefficient | — |

📄 **Example (`input.txt`):**
```
700  
350 
5000 
400 
500000 
5000 
250  
1.1  
1.2  
0.6
```

---

## ⚙️ How to Run

1. Make sure you have **Python 3.7+** installed.  
2. Place both `flexural_design.py` and `input.txt` in the same folder.  
3. Run the script:
   ```bash
   python flexural_design.py
   ```
4. The program will print the results in the terminal and also create an `output.txt` file with detailed results.

---

## 🧾 Output Example

```
The applied moment is safe. Moment capacity (Md): 440.91 kNm, Applied moment (M): 350 kNm.

The applied shear force is safe. Shear capacity (Vd): 272.73 kN, Applied shear (V): 700 kN.

Deflection Results:
Bending Deflection (mm): 5.12
Shear Deflection (mm): 0.84
Total Deflection (mm): 5.96
Permissible Deflection (mm): 16.67
Is Safe: Yes
Recommendation: Beam design is within permissible limits.
```

---

## 🧠 Concepts Used

- **Flexural design:**  
  \( M_d = \frac{β_b × Z_e × f_y}{γ_{m0}} \)

- **Shear design:**  
  \( V_d = \frac{τ_v × A_v × f_y}{γ_{m0}} \)

- **Deflection check (IS 800:2007):**  
  \( δ_{perm} = \frac{L}{300} \)

- **Total Deflection:**  
  Sum of bending and shear deflection components.

---

## 🧰 Dependencies

No external libraries required — uses only Python’s built-in modules.

---

## 👤 Author

**[prashant-106](https://github.com/prashant-106)**  
Civil Engineering Student | NIT Silchar  
📘 Project compliant with **IS 800:2007**
