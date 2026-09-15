ssr_pipeline.ipynb

Jupyter notebook (.ipynb) with the SSR filtering and genotyping pipeline for Dipteryx alata Vogel, using HipSTR and Tandem Repeat Finder guided by a reference genome.

Notebook structure
1. Docker environment — container setup using the weisburd/hipstr image
2. Dependency installation — system packages and Miniconda
3. SSR discovery (TRF) — Tandem Repeats Finder, quality filtering, and conversion to BED
4. Sequencing preprocessing — FastQC, fastp, alignment with bwa-mem2, sorting, and duplicate marking
5. HipSTR — genotyping of SSR regions and VCF filtering
6. TRTools — quality control (qcSTR), additional filtering (dumpSTR), and per-locus statistics (statSTR)

Notes
    Requires HipSTR, TRF, TRTools, bwa-mem2, samtools/bcftools, picard, and R packages (vcfR, dplyr, ggplot2, among others).
    For the descriptive statistics in R, check the scripts/R_scripts folder.