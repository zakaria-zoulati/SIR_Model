# SIR Epidemiological Model

## Table of Contents
- [Introduction](#introduction)
- [Mathematical Foundation](#mathematical-foundation)
- [Model Variants](#model-variants)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results and Visualizations](#results-and-visualizations)
- [Theory and Background](#theory-and-background)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

## Introduction

The SIR model is a fundamental epidemiological model used to describe the spread of infectious diseases through populations. This project implements both deterministic and stochastic versions of the SIR model, providing comprehensive analysis tools for understanding disease dynamics.

The model divides the population into three compartments:
- **S(t)**: Susceptible individuals who can contract the disease
- **I(t)**: Infected individuals who can transmit the disease
- **R(t)**: Recovered individuals who have immunity

## Mathematical Foundation

### Deterministic SIR Model

The deterministic SIR model is governed by the following system of ordinary differential equations:

```
dS/dt = -βSI/N
dI/dt = βSI/N - γI
dR/dt = γI
```

Where:
- `β` is the transmission rate
- `γ` is the recovery rate
- `N = S + I + R` is the total population (constant)

### Key Parameters

- **Basic Reproduction Number (R₀)**: `R₀ = β/γ`
  - If R₀ > 1, the disease spreads
  - If R₀ < 1, the disease dies out
  - If R₀ = 1, the disease is at equilibrium

- **Contact Rate**: Number of contacts per unit time that could lead to infection
- **Infectious Period**: Average time an individual remains infectious (1/γ)

### Stochastic SIR Model

The stochastic version incorporates randomness in the transmission and recovery processes, accounting for the inherent uncertainty in real-world epidemics. This is particularly important for:
- Small populations
- Early stages of epidemics
- Modeling extinction events

## Model Variants

This project implements multiple approaches:

1. **Deterministic ODE Solution** (`sir.py`)
   - Numerical integration using sophisticated ODE solvers
   - Deterministic trajectory analysis
   - Parameter sensitivity studies

2. **Stochastic Simulation** (`stochastic_model.py`)
   - Monte Carlo simulations
   - Gillespie algorithm implementation
   - Statistical analysis of multiple realizations

3. **Custom ODE Solver** (`ODESOLVER.py`)
   - Implementation of numerical methods
   - Runge-Kutta methods
   - Adaptive step-size control

## Project Structure

```
SIR_Model/
│
├── sir.py                      # Main deterministic SIR model
├── stochastic_model.py         # Stochastic SIR implementation
├── ODESOLVER.py               # Custom ODE solver implementations
├── SIR_Good_Theory.pdf        # Theoretical background document
├── README.md                  # This file
├── .gitignore                # Git ignore file
├── images/                    # Visualization outputs
│   ├── static.png            # Deterministic model results
│   ├── Stochastic1.png       # Stochastic simulation results
│   └── Stochastic2.png       # Additional stochastic analysis
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/SIR_Model.git
   cd SIR_Model
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv sir_env
   source sir_env/bin/activate  # On Windows: sir_env\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install numpy scipy matplotlib pandas seaborn
   ```

## Usage

### Running the Deterministic Model

```python
python sir.py
```

This will generate the deterministic SIR model solution and create visualizations showing the evolution of S, I, and R populations over time.

### Running the Stochastic Model

```python
python stochastic_model.py
```

This performs multiple stochastic simulations and generates statistical analyses of the epidemic dynamics.

### Custom ODE Solver

```python
from ODESOLVER import *

# Example usage of custom solver
# (Implementation depends on your specific solver structure)
```

### Parameter Configuration

Modify the model parameters in the respective Python files:

```python
# Example parameter set
beta = 0.3      # Transmission rate
gamma = 0.1     # Recovery rate
N = 1000        # Total population
I0 = 1          # Initial infected
S0 = N - I0     # Initial susceptible
R0 = 0          # Initial recovered
```

## Results and Visualizations

### Deterministic Model Results
![Static SIR Model](images/deterministic.png)
*Deterministic SIR model showing the classic epidemic curve with susceptible (blue), infected (red), and recovered (green) populations.*

### Stochastic Model Results
![Stochastic SIR Model 1](images/Stochastic1.png)
*Multiple realizations of the stochastic SIR model showing variability in epidemic trajectories.*

![Stochastic SIR Model 2](images/Stochastic2.png)
*Statistical analysis of stochastic simulations including confidence intervals and probability distributions.*

## Theory and Background

### Epidemic Phases

1. **Initial Growth Phase**: Exponential increase in infected individuals
2. **Peak Phase**: Maximum number of infected individuals
3. **Decay Phase**: Decline in infected population as herd immunity develops

### Herd Immunity Threshold

The herd immunity threshold is reached when:
```
S/N < 1/R₀
```

At this point, the effective reproduction number falls below 1, and the epidemic begins to decline.

### Model Assumptions

- **Homogeneous mixing**: All individuals have equal contact rates
- **Permanent immunity**: Recovered individuals cannot be reinfected
- **Constant population**: No births, deaths, or migration
- **Instantaneous recovery**: No latent period

### Limitations and Extensions

- Real epidemics may require more complex models (SEIR, SEIRS, etc.)
- Spatial heterogeneity and network effects
- Age-structured populations
- Vaccination strategies
- Behavioral changes during epidemics


**Note**: For detailed mathematical derivations and theoretical analysis, please refer to the included `SIR_Good_Theory.pdf` document.