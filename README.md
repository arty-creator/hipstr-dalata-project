This repository contains the scripts, workflows, supporting files, and data analysis used for the in silico genotyping and characterization of Simple Sequence Repeats (SSRs) from whole-genome sequencing (WGS) data for the manuscript:

**In silico genome-wide identification and characterization of microsatellite loci in baru tree (*Dipteryx alata*) using resequencing whole genome sequencing data**

The repository is intended to support the reproducibility of the analyses presented in the manuscript.

---

## SSR Characterization Pipeline for *Dipteryx alata*

### Overview

This pipeline performs the identification, *in silico* genotyping, and characterization of microsatellite markers (SSRs) from low-coverage whole-genome sequencing (lcWGS) data for *Dipteryx alata* (baru tree), a species native to the Brazilian Cerrado.

This work forms Chapter 1 of a master's dissertation organized as a collection of articles, focusing on the characterization of genomic resources for this species.

The workflow integrates four main tools — **TRF**, **HipSTR**, **TRTools**, and **VariantAnnotation** — each responsible for a distinct stage: structural repeat discovery, empirical genotyping from sequencing data, filtering and post-genotyping statistics, and genomic localization of the loci.

---

## Input Data

The pipeline uses the following data:

* Whole-genome sequencing (WGS) data, with approximately 9–14× coverage;
* 24 *Dipteryx alata* individuals;
* Data previously processed through quality control using FastQC and adapter/quality trimming with fastp from raw FASTQ files;
* Read-group metadata added during alignment using `bwa mem -R`, followed by read sorting with samtools and duplicate marking with Picard MarkDuplicates.

Raw sequencing data and other large files are not included directly in this repository. Their availability and corresponding access identifiers are documented in the **Data Availability** section and in [data/README.md](data/README.md).

---

## Conceptual Structure: Three Datasets

The pipeline generates three datasets representing different analytical layers, unified by the concept of **ascertainment bias**. Each layer incorporates a new potential source of cumulative bias.

| Dataset               | Description                                                                       | Source of bias                                       |
| --------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **1. Discovery**      | Repeats structurally identified in the reference genome                           | Structural detection bias inherent to TRF            |
| **2. Genotyping**     | Loci effectively genotyped in the sequenced individuals                           | Structural detection bias + sampling bias            |
| **3. High confidence**| Genotyped loci meeting the established quality and coverage criteria              | Structural detection bias + sampling + coverage     |

This layered structure represents the **structural potential**, **empirical detectability**, and **applied robustness** of the identified markers, respectively.

---

## Pipeline Stages

### 1. Repeat Discovery — TRF

Exploratory identification of repetitive regions in the reference genome using **Tandem Repeats Finder (TRF)**.

Copy number, period, and other array characteristics are obtained as algorithm outputs and do not represent targeted search parameters.

### 2. Coordinate Extraction and Processing — BED

Conversion and processing of the identified loci coordinates into BED format, accounting for the difference between coordinate systems.

This stage preserves the distinction between **total array length**, **motif period**, and **copy number**.

### 3. *In Silico* Genotyping — HipSTR

The identified loci are genotyped directly from the 24 individuals' lcWGS data using **HipSTR**.

This stage produces genotypes for the SSR loci identified in the reference genome and provides the basis for subsequent filtering and characterization analyses.

### 4. Filtering and Statistics — TRTools

Genotyping results are processed using **TRTools**, including locus filtering, variant-file processing, and generation of descriptive statistics.

This stage defines the high-confidence dataset and characterizes the loci according to their respective motif classes.

### 5. Genomic Localization — VariantAnnotation

The loci are annotated using **VariantAnnotation** (Bioconductor/R) and classified according to their genomic location, including genic and intergenic regions. This stage does not infer protein effects or frameshifts.

This classification supports the interpretation of the markers' potential applications in subsequent studies, including diversity, population genetics, neutrality, and possible phenotype-association analyses.

---

## Tools Used

| Tool                            | Function                                                       |
| ------------------------------- | -------------------------------------------------------------- |
| **TRF (Tandem Repeats Finder)** | Structural identification of repetitive regions                |
| **HipSTR**                      | STR genotyping from sequencing data                            |
| **TRTools**                     | Filtering, conversion, and statistical analysis of genotyped STRs |
| **VariantAnnotation**           | Variant annotation and manipulation in Bioconductor/R          |

Specific versions of the tools and packages used are listed in the `environment/` directory.

---

## Repository Structure

```text
hipstr-dalata-project/
│
├── README.md
├── CITATION.cff
├── .gitignore
│
├── scripts/
│   ├── pipeline/
│   │   ├── README.md
│   │   └── ssr_pipeline.ipynb
│   └── R_scripts/
│       ├── README.md
│       └── *.Rmd
│
├── data/
│   └── README.md
│
├── results/*.csv
│
├── environment/
│   └── README.md
```

### Directory Description

* `scripts/pipeline/` — main notebook for discovery, genotyping, and filtering;
* `scripts/R_scripts/` — descriptive analyses and genomic localization in R Markdown;
* `data/` — links and metadata for the external files required for execution;
* `results/` — selected tabular results;
* `environment/` — information about tool, package, and dependency versions.

Large files, such as FASTQ, BAM, and complete VCF files, are not stored directly in this repository.

---

## Reprodutibilidade

The scripts provided in this repository correspond to the computational stages used to generate the results presented in the manuscript.

Whenever possible, the analysis parameters are specified directly in the scripts or in associated configuration files.

The versions of the tools and packages used are documented in the `environment/` directory.

The relationship between scripts, input files, and results is documented throughout the repository to facilitate reproduction of the analyses.

---

## Data Availability

Raw sequencing data and other large input files are not included in this repository.

Links to the sequencing data, reference genome, annotation files, and other external resources are listed in [data/README.md](data/README.md), together with the filenames expected by the scripts.

---

## Citation

If you use the scripts, workflows, or other resources provided in this repository, please cite the associated manuscript.

Citation information is also provided in `CITATION.cff`.

---

## License

The scripts developed for this project are distributed under the **MIT License**.

Third-party software, reference genomes, annotation files, databases, and other externally sourced resources are subject to their respective licenses and terms of use.

See the `LICENSE` file for details when the license is added to the repository.

---

## Status

This repository is associated with a manuscript currently under preparation/submission.

The repository may be updated as the manuscript and associated analyses progress.
