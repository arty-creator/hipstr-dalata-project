# Dados e arquivos externos

Os dados brutos de sequenciamento e outros arquivos grandes usados pelo pipeline não são versionados neste repositório. O VCF filtrado está disponível compactado em `hipstr_post_dumpstr_filtered_mq1.rar`. Confirme os nomes dos arquivos extraídos antes de executar as análises.

## Recursos necessários

| Recurso | Arquivo esperado | Link de acesso |
|---|---|---|
| Leituras paired-end | `*_R1_001.fastq.gz`, `*_R2_001.fastq.gz` | A preencher |
| Genoma de referência | `genome.fasta` e índice `.fai` | A preencher |
| Anotação gênica | `mikado.loci.clean.step2.primaryTranscripts.gff3` | A preencher |
| VCF Dataset 2 — genotipagem HipSTR | `hipstr_mq1.vcf` | Gerado pelo pipeline |
| VCF Dataset 3 — após filtragem TRTools | `hipstr_post_dumpstr_filtered_mq1.vcf` | Arquivo compactado neste repositório |

Os links dos dados externos devem apontar para uma fonte estável e, quando disponível, incluir accession, DOI ou identificador equivalente. Registre também o checksum dos arquivos para permitir a conferência da versão utilizada no artigo.

Os caminhos locais usados no notebook podem ser ajustados para a organização da máquina de execução, mas os nomes dos arquivos devem permanecer consistentes com esta tabela ou ser alterados nas etapas correspondentes do pipeline.
