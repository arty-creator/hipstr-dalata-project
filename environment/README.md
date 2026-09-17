# Environment — ssr_pipeline

Tools and packages used in the pipeline. The VCF filtering step (`filter_vcf.py`) requires a separate Python environment (see final section).

## Main environment

### Sequencing QC and preprocessing
| Tool | Version |
|---|---|
| FastQC | 0.12.1 |
| Fastp | 0.23.2 |
| BWA-MEM2 | 2.1 |
| SAMtools | 1.23.1 |
| Picard | 3.4.0 |

### SSR discovery and genotyping
| Tool | Version |
|---|---|
| TRF (Tandem Repeats Finder) | 4.10.0rc2 |
| HipSTR | 0.6.2 |
| TRTools (qcSTR, dumpSTR, statSTR) | — |

### R
| Package | Version |
|---|---|
| R (base) | 4.5.2 |

**Bioconductor**
- VariantAnnotation (1.56.0)
- GenomicFeatures
- txdbmaker
- GenomicRanges
- GenomeInfoDb
- IRanges
- Biostrings
- rtracklayer
- Rsamtools

**CRAN**
- dplyr, tidyr, stringr, forcats, purrr, tibble, readr, tidyverse
- ggplot2, scales, patchwork, ggthemes, ggridges, ggrepel
- vcfR
- DT, kableExtra, writexl

## Separate environment: VCF filtering (HipSTR)

The `filter_vcf.py` script depends on PyVCF, which requires Python 3.8:

| Package | Version |
|---|---|
| Python | 3.8 |
| setuptools | <58 |
| PyVCF | — |