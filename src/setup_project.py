"""
TW5 Project Setup Script
Creates necessary folders for the project
"""

import os

# Create directory structure
directories = [
    'src',
    'results',
    'results/slln',
    'results/clt',
    'reports'
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"✓ Created directory: {directory}")

print("\n" + "="*60)
print("Project structure created successfully!")
print("="*60)
print("\nNext steps:")
print("1. Run: python src/distributions_info.py")
print("2. Run: python src/slln_analysis.py")
print("3. Run: python src/clt_analysis.py")
print("4. Run: python src/comparative_analysis.py")
