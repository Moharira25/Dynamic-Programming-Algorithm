# Inventory Management Problem

This repository contains the coursework submitted for the **CO3002 - Analysis and Design of Algorithms** module. The project focuses on solving an inventory management optimization problem using algorithmic techniques.

---

## 📄 Problem Description

The objective is to determine the **optimal daily order quantities** for a warehouse over `n` days, given a known sequence of daily demands. The aim is to **minimize total cost**, which includes:

- A **fixed delivery cost** `K` per order
- A **daily storage cost** `C` per item
- A **maximum storage capacity** `S` that cannot be exceeded

---

## 🧠 Solution Overview

The solution consists of two main components, see the report: **`Algorithm_Design_and_Analysis_CW.pdf`** for full details:

### ✅ Greedy Algorithm Counter-Example

A counter-example is included to show that a naive greedy strategy does **not always lead to the optimal solution**.

### 💡 Dynamic Programming Algorithm

An efficient bottom-up **Dynamic Programming (DP)** algorithm was developed:

- `cost[i][j]` stores the minimum cost up to day `i` with `j` items left in inventory.
- A **traceback mechanism** reconstructs the optimal sequence of order quantities.

#### 📊 Complexity Analysis

- **Time Complexity:** O(n × S²)  
- **Space Complexity:** O(n × S)

---

## 📁 Files in this Repository

- `Algorithm_Design_and_Analysis_CW.pdf` — Full report with problem description, algorithm design, and analysis  
- `AlgorithmImplementation.py` — Python script implementing the dynamic programming solution

---

## ▶️ How to Run

Run the script from the command line:

```bash
python AlgorithmImplementation.py
````

* Input parameters (`S`, `C`, `K`, `n`, `demands`) are hardcoded at the bottom of the script.
* You can edit these values to test different demand sequences or warehouse configurations.

---

## 🖨️ Example Output

Upon execution, the script will display:

* ✅ The **minimum total cost**
* 📈 The complete **cost (DP) table**
* 🔁 The **traceback table** for reconstructing the solution
* 📦 The final list of **optimal order quantities per day**

