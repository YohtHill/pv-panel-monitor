#!/usr/bin/env python3
"""
Script to initialize Git repository for Group 8 PV Monitor Project
"""

import os
import subprocess
import sys

def run_command(cmd):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def main():
    print("Initializing Git repository for Group 8 PV Monitor Project...")
    print()
    
    # Initialize Git repository
    print("Step 1: Initializing Git repository...")
    retcode, stdout, stderr = run_command("git init")
    if retcode != 0:
        print(f"Error: {stderr}")
        return 1
    print("✓ Git repository initialized")
    
    # Add all files
    print("Step 2: Adding files to repository...")
    retcode, stdout, stderr = run_command("git add .")
    if retcode != 0:
        print(f"Error: {stderr}")
        return 1
    print("✓ Files added to staging area")
    
    # Create initial commit
    print("Step 3: Creating initial commit...")
    commit_message = """Initial commit: Photovoltaic Panel Parameter Monitor Project

- STM32F042K6 microcontroller code
- ST7735 LCD display driver
- ADC voltage measurement implementation
- Project documentation and build instructions
- Team information and project summary"""
    
    retcode, stdout, stderr = run_command(f'git commit -m "{commit_message}"')
    if retcode != 0:
        print(f"Error: {stderr}")
        return 1
    print("✓ Initial commit created")
    
    print()
    print("=" * 60)
    print("Git repository initialized successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Create a new repository on GitHub")
    print("2. Add remote: git remote add origin [your-github-repo-url]")
    print("3. Push: git push -u origin main")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())