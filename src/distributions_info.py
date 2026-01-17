"""
TW5 - Distribution Definitions and Moment Calculations
Contains all 5 distributions with their properties
"""

import numpy as np

# Distribution Information Dictionary
distributions = {
    'Uniform(0,1)': {
        'mean': 0.5,
        'variance': 1/12,
        'std': np.sqrt(1/12),
        'pdf': 'f(x) = 1, 0 ≤ x ≤ 1',
        'generator': lambda n: np.random.uniform(0, 1, n),
        'slln_works': True,
        'clt_works': True,
        'notes': 'Classic case - both theorems work perfectly'
    },
    
    'Exponential(λ=1)': {
        'mean': 1.0,
        'variance': 1.0,
        'std': 1.0,
        'pdf': 'f(x) = e^(-x), x ≥ 0',
        'generator': lambda n: np.random.exponential(1, n),
        'slln_works': True,
        'clt_works': True,
        'notes': 'Skewed distribution - CLT slower due to asymmetry'
    },
    
    'Pareto(α=3, xₘ=1)': {
        'mean': 1.5,  # = α*xₘ/(α-1) = 3*1/(3-1) = 1.5
        'variance': 0.75,  # = α*xₘ²/((α-1)²(α-2)) = 3*1/((2)²(1)) = 3/4
        'std': np.sqrt(0.75),
        'pdf': 'f(x) = 3/x⁴, x ≥ 1',
        'generator': lambda n: (np.random.pareto(3, n) + 1),
        'slln_works': True,
        'clt_works': True,
        'notes': 'Heavy-tailed but finite variance - both theorems work'
    },
    
    'Pareto(α=1.5, xₘ=1)': {
        'mean': 3.0,  # = 1.5*1/(1.5-1) = 1.5/0.5 = 3
        'variance': np.inf,  # INFINITE! (α ≤ 2)
        'std': np.inf,
        'pdf': 'f(x) = 1.5/x^2.5, x ≥ 1',
        'generator': lambda n: (np.random.pareto(1.5, n) + 1),
        'slln_works': True,
        'clt_works': False,
        'notes': '⚠️ CRITICAL: Infinite variance! SLLN works but CLT does NOT!'
    },
    
    'Cauchy': {
        'mean': None,  # UNDEFINED!
        'variance': None,  # UNDEFINED!
        'std': None,
        'pdf': 'f(x) = 1/(π(1+x²))',
        'generator': lambda n: np.random.standard_cauchy(n),
        'slln_works': False,
        'clt_works': False,
        'notes': '⚠️ CRITICAL: Mean undefined! Neither theorem works!'
    }
}

# Print moment table
def print_moment_table():
    """Print formatted table of moments"""
    print("\n" + "="*80)
    print("MOMENT TABLE - TW5 DISTRIBUTIONS")
    print("="*80)
    print(f"{'Distribution':<25} {'E[X]':<15} {'Var(X)':<15} {'Notes'}")
    print("-"*80)
    
    for name, info in distributions.items():
        mean_str = f"{info['mean']:.4f}" if info['mean'] is not None else "UNDEFINED"
        var_str = f"{info['variance']:.4f}" if info['variance'] not in [None, np.inf] else ("INFINITE" if info['variance'] == np.inf else "UNDEFINED")
        
        print(f"{name:<25} {mean_str:<15} {var_str:<15}")
    
    print("="*80)
    
    # Print theoretical implications
    print("\nTHEORETICAL IMPLICATIONS:")
    print("-"*80)
    print("SLLN Requirements: E[X] < ∞")
    print("  ✓ Works for: Uniform, Exponential, Pareto(α=3), Pareto(α=1.5)")
    print("  ✗ Fails for: Cauchy (mean undefined)")
    print()
    print("CLT Requirements: E[X] < ∞ AND Var(X) < ∞")
    print("  ✓ Works for: Uniform, Exponential, Pareto(α=3)")
    print("  ✗ Fails for: Pareto(α=1.5) (infinite variance), Cauchy (undefined)")
    print("="*80)

if __name__ == "__main__":
    print_moment_table()
    
    # Test generators
    print("\nTesting generators (generating 5 samples from each):")
    print("-"*80)
    for name, info in distributions.items():
        np.random.seed(42)
        samples = info['generator'](5)
        print(f"{name}: {samples}")
    print("="*80)
