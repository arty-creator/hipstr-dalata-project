# hipstr-dalata-project

This repository contains the scripts, workflows, supporting files, and data analysis used for the in silico genotyping and characterization of Simple Sequence Repeats (SSRs) from whole-genome sequencing (WGS) data for the manuscript:

**In silico genome-wide identification and characterization of microsatellite loci in baru tree (*Dipteryx alata*) using resequencing whole genome sequencing data**

The repository is intended to support the reproducibility of the analyses presented in the manuscript.

---

## Pipeline de Caracterização de SSRs em *Dipteryx alata* (Baruzeiro)

### Visão Geral

Este pipeline realiza a identificação, genotipagem *in silico* e caracterização de marcadores microssatélites (SSRs) a partir de dados de sequenciamento de baixa cobertura (*low-coverage whole-genome sequencing*, lcWGS) de *Dipteryx alata* (baruzeiro), espécie nativa do Cerrado.

O trabalho compõe o Capítulo 1 de uma dissertação de mestrado organizada em formato de artigos, com foco na caracterização de recursos genômicos para a espécie.

O fluxo integra quatro ferramentas principais — **TRF**, **HipSTR**, **TRTools** e **VariantAnnotation** — cada uma responsável por uma etapa distinta do processo: descoberta estrutural de repetições, genotipagem empírica a partir de dados de sequenciamento, filtragem e geração de estatísticas pós-genotipagem e anotação funcional das variantes.

---

## Dados de Entrada

Os dados utilizados no pipeline consistem em:

* Dados de sequenciamento *whole-genome* de baixa cobertura (lcWGS), com aproximadamente 9–14× de cobertura;
* 24 indivíduos de *Dipteryx alata*;
* Dados previamente processados pelo pipeline **RIG** (*Recalibration and Interrelation of Genomic Sequence Data with the GATK*), a partir de arquivos FASTQ brutos;
* Metadados de *read groups* incorporados durante o processamento dos dados, utilizando `bwa mem -R`.

Os dados brutos de sequenciamento e outros arquivos de grande porte não são incluídos diretamente neste repositório. Quando aplicável, sua disponibilidade e respectivos identificadores de acesso são descritos na seção **Data Availability**.

---

## Estrutura Conceitual: Três Datasets

O pipeline gera três datasets que representam diferentes camadas analíticas, unificadas pelo conceito de **viés de ascertainment (ascertainment bias)**. Cada camada incorpora uma nova fonte potencial de viés cumulativo.

| Dataset               | Descrição                                                                         | Fonte de viés                                        |
| --------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **1. Descoberta**     | Repetições identificadas estruturalmente no genoma de referência                  | Viés de detecção estrutural, inerente ao TRF         |
| **2. Genotipagem**    | Loci efetivamente genotipados nos indivíduos sequenciados                         | Viés de detecção estrutural + viés de amostragem     |
| **3. Alta confiança** | Loci genotipados que atendem aos critérios de qualidade e cobertura estabelecidos | Viés de detecção estrutural + amostragem + cobertura |

Essa estrutura em camadas representa, respectivamente, o **potencial estrutural**, a **detectabilidade empírica** e a **robustez aplicada** dos marcadores identificados.

---

## Etapas do Pipeline

### 1. Descoberta de repetições — TRF

Identificação exploratória de regiões repetitivas no genoma de referência utilizando **Tandem Repeats Finder (TRF)**.

As informações de *copy number*, período e demais características dos arrays são obtidas como resultados do algoritmo e não representam parâmetros de busca direcionada.

### 2. Extração e tratamento das coordenadas — BED

Conversão e tratamento das coordenadas dos loci identificados para o formato BED, considerando adequadamente a diferença entre sistemas de coordenadas.

Essa etapa permite a obtenção das características dos arrays mantendo a distinção entre **comprimento total do array**, **período do motivo** e **número de cópias**.

### 3. Genotipagem *in silico* — HipSTR

Genotipagem dos loci identificados diretamente a partir dos dados de lcWGS dos 24 indivíduos utilizando **HipSTR**.

A etapa produz os genótipos dos loci SSR identificados no genoma de referência e constitui a base para as análises posteriores de filtragem e caracterização.

### 4. Filtragem e estatísticas — TRTools

Processamento dos resultados de genotipagem utilizando **TRTools**, incluindo filtragem dos loci, processamento dos arquivos de variantes e geração de estatísticas descritivas.

Essa etapa resulta na definição do dataset de alta confiança e na caracterização dos loci de acordo com suas respectivas classes de motivo.

### 5. Anotação funcional — VariantAnnotation

Anotação das variantes utilizando **VariantAnnotation** (Bioconductor/R), permitindo a classificação dos loci de acordo com sua localização genômica, incluindo regiões gênicas e intergênicas.

Essa classificação auxilia na interpretação do potencial de aplicação dos marcadores em estudos posteriores, incluindo análises de diversidade, genética populacional, neutralidade e possíveis associações com características fenotípicas.

---

## Ferramentas Utilizadas

| Ferramenta                      | Função                                                         |
| ------------------------------- | -------------------------------------------------------------- |
| **TRF (Tandem Repeats Finder)** | Identificação estrutural de regiões repetitivas                |
| **HipSTR**                      | Genotipagem de STRs a partir de dados de sequenciamento        |
| **TRTools**                     | Filtragem, conversão e análise estatística de STRs genotipados |
| **VariantAnnotation**           | Anotação e manipulação de variantes no ambiente Bioconductor/R |

As versões específicas das ferramentas e dos pacotes utilizados são apresentadas no diretório `environment/`.

---

## Estrutura do Repositório

```text
hipstr-dalata-project/
│
├── README.md
├── index.html
├── CITATION.cff
├── LICENSE
├── .gitignore
│
├── scripts/
│   ├── 01_trf/
│   ├── 02_coordinates/
│   ├── 03_hipstr/
│   ├── 04_trtools/
│   └── 05_annotation/
│
├── data/
│   └── README.md
│
├── results/
│   └── README.md
│
├── figures/
│
├── environment/
│   ├── environment.yml
│   └── versions.txt
│
└── docs/
    └── workflow.md
```

### Descrição dos diretórios

* `scripts/` — scripts utilizados nas diferentes etapas do pipeline;
* `data/` — arquivos de entrada ou exemplos necessários para execução dos scripts;
* `results/` — resultados selecionados das análises;
* `figures/` — figuras geradas a partir dos resultados;
* `environment/` — informações sobre versões de ferramentas, pacotes e dependências;
* `docs/` — documentação complementar sobre o fluxo de análise.

Arquivos de grande porte, como FASTQ, BAM e VCF completos, não são armazenados diretamente neste repositório.

---

## Reprodutibilidade

Os scripts disponibilizados neste repositório correspondem às etapas computacionais utilizadas para gerar os resultados apresentados no manuscrito.

Sempre que possível, os parâmetros utilizados nas análises são especificados diretamente nos scripts ou em arquivos de configuração associados.

As versões das ferramentas e dos pacotes utilizados são documentadas no diretório `environment/`.

A relação entre scripts, arquivos de entrada e resultados será indicada ao longo da documentação para facilitar a reprodução das análises.

---

## Data Availability

Raw sequencing data and other large input files are not included in this repository.

The availability of the original sequencing data, genome reference, annotation files, and other external resources is described in the manuscript and/or in the corresponding repository documentation.

---

## Citation

If you use the scripts, workflows, or other resources provided in this repository, please cite the associated manuscript.

Citation information is also provided in `CITATION.cff`.

---

## License

The scripts developed for this project are distributed under the **MIT License**.

Third-party software, reference genomes, annotation files, databases, and other externally sourced resources are subject to their respective licenses and terms of use.

See the `LICENSE` file for details.

---

## Status

This repository is associated with a manuscript currently under preparation/submission.

The repository may be updated as the manuscript and associated analyses progress.
