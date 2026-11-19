#!/usr/bin/env python3
"""
Generate comprehensive SSR summary statistics tables by chromosome

This script analyzes Tandem Repeat Finder (TRF) output to generate two complementary
tables for STR discovery characterization:
  1. Overview table: SSR counts, density, period distribution, and genomic coverage
  2. Detailed distribution: Length and copy number statistics per chromosome

Usage:
    python generate_ssr_summary_table.py <chromosome_sizes.txt> <str_final.tsv>

Input files:
    - chromosome_sizes.txt: Tab-separated file with chromosome name and size (bp)
    - str_final.tsv: Filtered STR regions with columns:
        chr, start, end, period_size, copy_number, pct_matches, pct_indels

Output files:
    - ssr_overview_table.tsv: Overview statistics (TSV format)
    - ssr_overview_table.txt: Overview statistics (formatted text)
    - ssr_detailed_distribution.tsv: Distribution statistics (TSV format)
    - ssr_detailed_distribution.txt: Distribution statistics (formatted text)

Author: Generated for STR discovery analysis
Version: 1.0
"""

import pandas as pd
import sys
import os

def load_chrom_sizes(chrom_sizes_file):
    """Load chromosome sizes from file"""
    chrom_sizes = {}
    with open(chrom_sizes_file, 'r') as f:
        for line in f:
            if line.strip():
                chrom, size = line.strip().split('\t')
                chrom_sizes[chrom] = int(size)
    return chrom_sizes

def calculate_ssr_overview(str_file, chrom_sizes):
    """Calculate overview SSR statistics per chromosome"""
    
    # Load STR data
    # Columns: chr, start, end, period_size, copy_number, %matches, %indels
    df = pd.read_csv(str_file, sep='\t', header=None,
                     names=['chr', 'start', 'end', 'period_size', 'copy_number', 
                            'pct_matches', 'pct_indels'])
    
    # Calculate STR length for each record
    df['str_length'] = df['end'] - df['start'] + 1
    
    # Group by chromosome and calculate statistics
    stats = []
    
    for chrom in sorted(chrom_sizes.keys()):
        chrom_data = df[df['chr'] == chrom]
        chrom_size = chrom_sizes[chrom]
        
        if len(chrom_data) > 0:
            num_ssrs = len(chrom_data)
            chrom_size_mb = chrom_size / 1_000_000
            ssrs_per_mb = num_ssrs / chrom_size_mb
            
            # Total SSR coverage
            total_ssr_length = chrom_data['str_length'].sum()
            pct_genome_in_ssrs = (total_ssr_length / chrom_size) * 100
            
            # Period size distribution
            period_1_2 = len(chrom_data[chrom_data['period_size'].isin([1, 2])])
            period_3 = len(chrom_data[chrom_data['period_size'] == 3])
            period_4_6 = len(chrom_data[chrom_data['period_size'].isin([4, 5, 6])])
            period_7_9 = len(chrom_data[chrom_data['period_size'].isin([7, 8, 9])])
            
            # Length and copy statistics
            mean_str_length = chrom_data['str_length'].mean()
            mean_copy = chrom_data['copy_number'].mean()
            median_copy = chrom_data['copy_number'].median()
            
            # Quality metrics
            mean_matches = chrom_data['pct_matches'].mean()
        else:
            num_ssrs = 0
            chrom_size_mb = chrom_size / 1_000_000
            ssrs_per_mb = 0
            total_ssr_length = 0
            pct_genome_in_ssrs = 0
            period_1_2 = period_3 = period_4_6 = period_7_9 = 0
            mean_str_length = mean_copy = median_copy = mean_matches = 0
        
        stats.append({
            'Chromosome': chrom,
            'Chr size (bp)': f"{chrom_size:,}",
            'No. of SSRs': num_ssrs,
            'SSRs/Mb': f"{ssrs_per_mb:.2f}",
            'Period 1-2': period_1_2,
            'Period 3': period_3,
            'Period 4-6': period_4_6,
            'Period 7-9': period_7_9,
            'Total SSR length (bp)': f"{total_ssr_length:,}",
            '% genome in SSRs': f"{pct_genome_in_ssrs:.3f}",
            'Mean STR length (bp)': f"{mean_str_length:.2f}",
            'Mean copy number': f"{mean_copy:.2f}",
            'Median copy number': f"{median_copy:.2f}",
            'Mean % matches': f"{mean_matches:.2f}"
        })
    
    # Add genome-wide totals
    total_size = sum(chrom_sizes.values())
    total_ssrs = len(df)
    total_size_mb = total_size / 1_000_000
    total_ssr_length = df['str_length'].sum()
    pct_genome_total = (total_ssr_length / total_size) * 100
    
    # Period totals
    period_1_2_total = len(df[df['period_size'].isin([1, 2])])
    period_3_total = len(df[df['period_size'] == 3])
    period_4_6_total = len(df[df['period_size'].isin([4, 5, 6])])
    period_7_9_total = len(df[df['period_size'].isin([7, 8, 9])])
    
    stats.append({
        'Chromosome': 'TOTAL',
        'Chr size (bp)': f"{total_size:,}",
        'No. of SSRs': total_ssrs,
        'SSRs/Mb': f"{total_ssrs / total_size_mb:.2f}",
        'Period 1-2': period_1_2_total,
        'Period 3': period_3_total,
        'Period 4-6': period_4_6_total,
        'Period 7-9': period_7_9_total,
        'Total SSR length (bp)': f"{total_ssr_length:,}",
        '% genome in SSRs': f"{pct_genome_total:.3f}",
        'Mean STR length (bp)': f"{df['str_length'].mean():.2f}",
        'Mean copy number': f"{df['copy_number'].mean():.2f}",
        'Median copy number': f"{df['copy_number'].median():.2f}",
        'Mean % matches': f"{df['pct_matches'].mean():.2f}"
    })
    
    return pd.DataFrame(stats)

def calculate_detailed_distribution(str_file, chrom_sizes):
    """Calculate detailed distribution statistics per chromosome"""
    
    # Load STR data
    df = pd.read_csv(str_file, sep='\t', header=None,
                     names=['chr', 'start', 'end', 'period_size', 'copy_number', 
                            'pct_matches', 'pct_indels'])
    
    df['str_length'] = df['end'] - df['start'] + 1
    
    # Group by chromosome and calculate detailed statistics
    stats = []
    
    for chrom in sorted(chrom_sizes.keys()):
        chrom_data = df[df['chr'] == chrom]
        
        if len(chrom_data) > 0:
            # Length distribution
            min_length = chrom_data['str_length'].min()
            median_length = chrom_data['str_length'].median()
            mean_length = chrom_data['str_length'].mean()
            max_length = chrom_data['str_length'].max()
            
            # Copy number distribution
            min_copy = chrom_data['copy_number'].min()
            median_copy = chrom_data['copy_number'].median()
            mean_copy = chrom_data['copy_number'].mean()
            max_copy = chrom_data['copy_number'].max()
            
            # Period size distribution
            mean_period = chrom_data['period_size'].mean()
            median_period = chrom_data['period_size'].median()
            
            # Spacing between SSRs
            mean_spacing = chrom_sizes[chrom] / len(chrom_data) if len(chrom_data) > 0 else 0
        else:
            min_length = median_length = mean_length = max_length = 0
            min_copy = median_copy = mean_copy = max_copy = 0
            mean_period = median_period = 0
            mean_spacing = 0
        
        stats.append({
            'Chromosome': chrom,
            'Min length (bp)': int(min_length),
            'Median length (bp)': f"{median_length:.1f}",
            'Mean length (bp)': f"{mean_length:.2f}",
            'Max length (bp)': int(max_length),
            'Min copy #': f"{min_copy:.2f}",
            'Median copy #': f"{median_copy:.2f}",
            'Mean copy #': f"{mean_copy:.2f}",
            'Max copy #': f"{max_copy:.2f}",
            'Mean period size': f"{mean_period:.2f}",
            'Median period size': f"{median_period:.1f}",
            'Mean spacing (bp)': f"{mean_spacing:,.0f}"
        })
    
    # Add genome-wide statistics
    if len(df) > 0:
        total_size = sum(chrom_sizes.values())
        mean_spacing_total = total_size / len(df)
        
        stats.append({
            'Chromosome': 'TOTAL',
            'Min length (bp)': int(df['str_length'].min()),
            'Median length (bp)': f"{df['str_length'].median():.1f}",
            'Mean length (bp)': f"{df['str_length'].mean():.2f}",
            'Max length (bp)': int(df['str_length'].max()),
            'Min copy #': f"{df['copy_number'].min():.2f}",
            'Median copy #': f"{df['copy_number'].median():.2f}",
            'Mean copy #': f"{df['copy_number'].mean():.2f}",
            'Max copy #': f"{df['copy_number'].max():.2f}",
            'Mean period size': f"{df['period_size'].mean():.2f}",
            'Median period size': f"{df['period_size'].median():.1f}",
            'Mean spacing (bp)': f"{mean_spacing_total:,.0f}"
        })
    
    return pd.DataFrame(stats)

def main():
    """Main execution function"""
    
    # Validate command line arguments
    if len(sys.argv) != 3:
        print(__doc__)
        print("\nError: Incorrect number of arguments")
        print("Usage: python generate_ssr_summary_table.py <chromosome_sizes.txt> <str_final.tsv>")
        sys.exit(1)
    
    chrom_sizes_file = sys.argv[1]
    str_file = sys.argv[2]
    
    # Validate input files exist
    if not os.path.exists(chrom_sizes_file):
        print(f"Error: Chromosome sizes file not found: {chrom_sizes_file}")
        sys.exit(1)
    
    if not os.path.exists(str_file):
        print(f"Error: STR file not found: {str_file}")
        sys.exit(1)
    
    # Set pandas display options for better formatting
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    print("="*80)
    print("SSR SUMMARY TABLE GENERATOR")
    print("="*80)
    print()
    
    # Load chromosome sizes
    print(f"[1/4] Loading chromosome sizes from: {chrom_sizes_file}")
    try:
        chrom_sizes = load_chrom_sizes(chrom_sizes_file)
        print(f"      ✓ Loaded {len(chrom_sizes)} chromosomes")
    except Exception as e:
        print(f"      ✗ Error loading chromosome sizes: {e}")
        sys.exit(1)
    
    # Calculate overview statistics
    print(f"\n[2/4] Calculating overview statistics from: {str_file}")
    try:
        overview_df = calculate_ssr_overview(str_file, chrom_sizes)
        print(f"      ✓ Generated overview table with {len(overview_df)} rows")
    except Exception as e:
        print(f"      ✗ Error calculating overview: {e}")
        sys.exit(1)
    
    # Calculate detailed distribution statistics
    print(f"\n[3/4] Calculating detailed distribution statistics")
    try:
        detailed_df = calculate_detailed_distribution(str_file, chrom_sizes)
        print(f"      ✓ Generated distribution table with {len(detailed_df)} rows")
    except Exception as e:
        print(f"      ✗ Error calculating distribution: {e}")
        sys.exit(1)
    
    # Save all output files
    print(f"\n[4/4] Saving output files")
    
    try:
        # Save TSV files
        overview_tsv = 'ssr_overview_table.tsv'
        overview_df.to_csv(overview_tsv, sep='\t', index=False)
        print(f"      ✓ {overview_tsv}")
        
        detailed_tsv = 'ssr_detailed_distribution.tsv'
        detailed_df.to_csv(detailed_tsv, sep='\t', index=False)
        print(f"      ✓ {detailed_tsv}")
        
        # Save formatted text files
        overview_txt = 'ssr_overview_table.txt'
        with open(overview_txt, 'w') as f:
            f.write("="*150 + "\n")
            f.write("TABLE 1: SSR OVERVIEW - DISCOVERY CHARACTERIZATION\n")
            f.write("="*150 + "\n")
            f.write(overview_df.to_string(index=False) + "\n")
            f.write("="*150 + "\n")
        print(f"      ✓ {overview_txt}")
        
        detailed_txt = 'ssr_detailed_distribution.txt'
        with open(detailed_txt, 'w') as f:
            f.write("="*150 + "\n")
            f.write("TABLE 2: DETAILED DISTRIBUTION STATISTICS\n")
            f.write("="*150 + "\n")
            f.write(detailed_df.to_string(index=False) + "\n")
            f.write("="*150 + "\n")
        print(f"      ✓ {detailed_txt}")
        
    except Exception as e:
        print(f"      ✗ Error saving files: {e}")
        sys.exit(1)
    
    # Display summary
    print()
    print("="*150)
    print("TABLE 1: SSR OVERVIEW - DISCOVERY CHARACTERIZATION")
    print("="*150)
    print(overview_df.to_string(index=False))
    print("="*150)
    print()
    print("="*150)
    print("TABLE 2: DETAILED DISTRIBUTION STATISTICS")
    print("="*150)
    print(detailed_df.to_string(index=False))
    print("="*150)
    print()
    
    print("="*80)
    print("✓ ANALYSIS COMPLETE")
    print("="*80)
    print("\nOutput files generated:")
    print(f"  • {overview_tsv} (machine-readable)")
    print(f"  • {overview_txt} (human-readable)")
    print(f"  • {detailed_tsv} (machine-readable)")
    print(f"  • {detailed_txt} (human-readable)")
    print()

if __name__ == "__main__":
    main()
