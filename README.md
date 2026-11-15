# Asset Portfolio Optimization Under Uncertainty

### Bachelor's Thesis Project — Amirkabir University of Technology

**Author:** Maryam Abedini  
**Degree:** B.Sc. in Mathematics and Applications  
**University:** Amirkabir University of Technology, Tehran, Iran  
**Supervisor:** Dr. Farnaz Hooshmand Khaligh
**Project Examiner:** Dr. Erfan Salavati
**Project Completion:** May 2025

---

## 1. Project Overview

This repository contains the original Python implementations developed for my bachelor's thesis, "Asset Portfolio Optimization Under Uncertainty," completed at Amirkabir University of Technology in May 2025.

The project investigates mathematical optimization approaches for portfolio selection under uncertainty in asset returns. Its primary objective is to examine how different uncertainty sets influence portfolio allocations, objective values, and the trade-off between expected return and robustness.

The study considers nominal portfolio optimization and several robust optimization formulations, incorporating cardinality constraints and lower and upper bounds on individual asset allocations.

The mathematical models were implemented in Python using Pyomo, with GAMS used as the optimization interface.

## 2. Mathematical Framework

The portfolio selection problem considers a set of available assets. Each asset is associated with an estimated expected return and, where applicable, an uncertainty parameter representing potential deviations from that estimate.

The decision variables determine the fraction of capital allocated to each asset.

The cardinality-constrained formulations impose the following requirements:

- The total portfolio allocation equals 100% of the available capital.
- Exactly a predetermined number of assets are selected.
- The allocation to each selected asset respects specified lower and upper bounds.
- Short selling is not permitted.

The robust formulations account for adverse deviations in estimated asset returns and seek allocations that remain effective under their respective uncertainty assumptions.

## 3. Optimization Models

The thesis investigates the following approaches.

### 3.1. Nominal Portfolio Optimization

The nominal formulation maximizes estimated portfolio return without explicitly accounting for uncertainty in the estimated returns.

It provides a benchmark for comparing the effects of robust optimization.

### 3.2. Markowitz-Type Portfolio Optimization

The study also considers portfolio optimization formulations incorporating risk-related constraints.

The corresponding Python scripts include exploratory quadratic-risk formulations. Their covariance assumptions and numerical parameters require further verification before they can be regarded as validated implementations of classical mean–variance portfolio optimization.

### 3.3. Box Uncertainty Set

The box uncertainty approach assumes that the deviation of each uncertain return parameter is independently bounded.

The resulting robust counterpart protects the portfolio against simultaneous adverse deviations across the uncertainty set.

### 3.4. Ellipsoidal Uncertainty Set

The ellipsoidal formulation uses a Euclidean-norm uncertainty set.

Compared with box uncertainty, this approach restricts the combinations of deviations that may occur simultaneously, providing a different balance between protection and conservatism.

### 3.5. Diamond Uncertainty Set

The diamond formulation uses an uncertainty set defined by the L1 norm.

Its robust counterpart involves the infinity norm of the weighted uncertainty coefficients, producing a different portfolio allocation structure from the box and ellipsoidal approaches.

### 3.6. Bertsimas–Sim Budgeted Uncertainty

The Bertsimas–Sim approach introduces an uncertainty-budget parameter, Γ, to control the degree of conservatism.

When Γ equals zero, the robust objective reduces to the nominal objective. Increasing Γ allows a larger aggregate adverse deviation, while Γ equal to the number of uncertain parameters recovers the full box-uncertainty protection under the standard assumptions.

## 4. Numerical Experiments

Two numerical settings were considered in the thesis.

### 4.1. Synthetic Dataset

The synthetic experiment consists of 10 assets, each characterized by three return scenarios.

The optimization models use the following portfolio constraints:

- Number of selected assets: 4
- Minimum allocation per selected asset: 1%
- Maximum allocation per selected asset: 50%

This experiment was designed to compare model behavior under controlled uncertainty conditions.

### 4.2. Real-Market Dataset

The real-market experiment considers 20 Iranian investment funds from different investment categories.

The historical data were obtained from the Tehran Securities Exchange Technology Management Company (TSETMC), as described in the thesis.

The thesis considers a 365-day historical period, with 300 days used for estimating model parameters and the remaining 65 days reserved for out-of-sample evaluation.

The portfolio constraints are:

- Number of selected assets: 5
- Minimum allocation per selected asset: 1%
- Maximum allocation per selected asset: 30%

The investigation compares portfolio allocations across the different optimization models and studies the effect of changing the uncertainty-budget parameter.

## 5. Implementation

**Programming Language:** Python  
**Optimization Modeling Framework:** Pyomo  
**Optimization Software:** GAMS

The repository includes the original Python scripts for the nominal, Markowitz-type, box, ellipsoidal, diamond, and budgeted-uncertainty formulations.

Separate scripts were developed for the synthetic and real-market numerical settings.

The implementations generally use fixed numerical parameters within the Python files rather than loading the complete historical datasets.

## 6. Repository Contents

The original filenames have been preserved to maintain the historical structure of the project.

**Nominal and Markowitz-Type Models**

- `Markovitz.py`
- `MarkovitzReal.py`

**Box Uncertainty Models**

- `Box.py`
- `Boxreal.py`

**Ellipsoidal Uncertainty Models**

- `Ellip.py`
- `Ellipreal.py`

**Diamond Uncertainty Models**

- `Diamond.py`
- `Diamondreal.py`

**Bertsimas–Sim Models**

- `bertsimas.py`
- `Bertsimasreal.py`

## 7. Academic Context

This project was completed as part of the requirements for the Bachelor of Science degree in Mathematics and Applications at Amirkabir University of Technology.

The research focuses on robust optimization techniques for financial decision-making and the application of mathematical programming to uncertainty-aware portfolio allocation.
