"""
TW5 - SLLN Analysis for All Distributions
Generates cumulative mean plots and analyzes convergence behavior
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Eğer distributions_info dosyası sende yoksa test için bu kısmı kullanabilirsin:
# from distributions_info import distributions

def slln_analysis(dist_name, generator, true_mean=None, n=10000, seed=42):
    """
    Perform SLLN analysis for a given distribution
    """
    np.random.seed(seed)
    
    # Klasör yoksa oluştur (Hata almamak için eklendi)
    if not os.path.exists('results/slln'):
        os.makedirs('results/slln', exist_ok=True)
    
    # Generate samples
    samples = generator(n)
    
    # Calculate cumulative mean
    cumulative_mean = np.cumsum(samples) / np.arange(1, n+1)
    
    # Create plot
    plt.figure(figsize=(14, 7))
    plt.plot(cumulative_mean, linewidth=0.8, color='blue', alpha=0.7)
    
    # Add true mean line if defined
    if true_mean is not None:
        plt.axhline(y=true_mean, color='red', linestyle='--', 
                    linewidth=2, label=f'True Mean μ = {true_mean}')
    
    plt.xlabel('Sample Size (n)', fontsize=13)
    plt.ylabel('Cumulative Mean', fontsize=13)
    plt.title(f'SLLN Convergence Analysis - {dist_name}', 
              fontsize=15, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Add statistics box
    if true_mean is not None:
        final_mean = cumulative_mean[-1]
        error = abs(final_mean - true_mean)
        
        # Find convergence points
        tolerance_01 = np.where(np.abs(cumulative_mean - true_mean) < 0.01)[0]
        conv_point_01 = tolerance_01[0] if len(tolerance_01) > 0 else n
        
        stats_text = f'Final Mean: {final_mean:.6f}\n'
        stats_text += f'True Mean: {true_mean:.6f}\n'
        stats_text += f'Final Error: {error:.6f}\n'
        stats_text += f'Converged (±0.01) at n ≈ {conv_point_01}'
        
        plt.text(0.02, 0.98, stats_text,
                transform=plt.gca().transAxes, 
                verticalalignment='top',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    else:
        # For Cauchy
        stats_text = f'Mean: UNDEFINED\n'
        stats_text += f'Sample Mean at n={n}: {cumulative_mean[-1]:.6f}\n'
        stats_text += f'⚠️ SLLN does NOT apply!'
        
        plt.text(0.02, 0.98, stats_text,
                transform=plt.gca().transAxes, 
                verticalalignment='top',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
    
    if true_mean is not None:
        plt.legend(fontsize=11)
    
    plt.tight_layout()
    
    # Save figure
    filename = dist_name.replace('(', '_').replace(')', '').replace(',', '').replace('=', '')
    plt.savefig(f'results/slln/slln_{filename}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return cumulative_mean

def analyze_all_distributions():
    """Run SLLN analysis for all distributions"""
    
    print("\n" + "="*80)
    print("SLLN ANALYSIS - ALL DISTRIBUTIONS")
    print("="*80)
    
    results = {}
    
    for dist_name, info in distributions.items():
        print(f"\n{'─'*80}")
        print(f"Analyzing: {dist_name}")
        print(f"{'─'*80}")
        print(f"PDF: {info['pdf']}")
        print(f"E[X]: {info['mean']}")
        print(f"Var(X): {info['variance']}")
        print(f"Expected SLLN behavior: {'Works' if info['slln_works'] else 'Does NOT work'}")
        
        # Run analysis
        cumulative_mean = slln_analysis(
            dist_name, 
            info['generator'], 
            info['mean'],
            n=10000
        )
        
        # Store results
        results[dist_name] = {
            'cumulative_mean': cumulative_mean,
            'final_mean': cumulative_mean[-1],
            'true_mean': info['mean']
        }
        
        # Print observations
        if info['mean'] is not None:
            final_error = abs(cumulative_mean[-1] - info['mean'])
            print(f"\n✓ Analysis complete")
            print(f"  Final sample mean: {cumulative_mean[-1]:.6f}")
            print(f"  True mean: {info['mean']:.6f}")
            print(f"  Final error: {final_error:.6f}")
            
            last_1000 = cumulative_mean[-1000:]
            volatility = np.std(last_1000)
            print(f"  Volatility (last 1000): {volatility:.6f}")
            
            if volatility < 0.01:
                print(f"  ✓ CONVERGED - Low volatility indicates stable convergence")
            else:
                print(f"  ~ Slow convergence - Higher volatility observed")
        else:
            print(f"\n✗ Mean is UNDEFINED")
            print(f"  Sample mean at n=10000: {cumulative_mean[-1]:.6f}")
            print(f"  ⚠️ SLLN DOES NOT APPLY - No convergence expected")
            
            last_1000 = cumulative_mean[-1000:]
            volatility = np.std(last_1000)
            print(f"  Volatility (last 1000): {volatility:.6f}")
            print(f"  Notice: High volatility - cumulative mean keeps fluctuating")
    
    print("\n" + "="*80)
    print("SLLN ANALYSIS COMPLETE - All plots saved to results/slln/")
    print("="*80)
    
    return results

if __name__ == "__main__":
    # distributions_info.py'den gelen verinin yapısı buna benzemeli:
    # results = analyze_all_distributions() 
    
    # Hata almamak için alt kısmı sadece data varsa çalışacak şekilde düzelttik:
    try:
        results = analyze_all_distributions()
        
        print("\n" + "="*80)
        print("SUMMARY: SLLN CONVERGENCE")
        print("="*80)
        print(f"{'Distribution':<25} {'True Mean':<12} {'Final Mean':<12} {'Error':<12} {'Status'}")
        print("-" * 80)
        
        for dist_name, info in distributions.items():
            if info['mean'] is not None:
                final_mean = results[dist_name]['final_mean']
                error = abs(final_mean - info['mean'])
                status = "✓ Converged" if error < 0.01 else "~ Slow"
                print(f"{dist_name:<25} {info['mean']:<12.6f} {final_mean:<12.6f} {error:<12.6f} {status}")
            else:
                final_mean = results[dist_name]['final_mean']
                print(f"{dist_name:<25} {'UNDEFINED':<12} {final_mean:<12.6f} {'N/A':<12} {'✗ No conv.'}")
        
        print("="*80)
    except NameError:
        print("Hata: 'distributions' verisi bulunamadı. Lütfen distributions_info.py dosyasını kontrol edin.")
