# Dados externos

Os arquivos grandes usados pelo pipeline não são versionados neste repositório. Use os links abaixo para obter os dados necessários e confirme os nomes dos arquivos antes de executar o pipeline.

## Recursos necessários

| Recurso | Arquivo esperado | Link de acesso |
|---|---|---|
| Leituras paired-end | `*_R1_001.fastq.gz`, `*_R2_001.fastq.gz` | A preencher |
| Genoma de referência | `genome.fasta` e índice `.fai` | A preencher |
| Anotação gênica | `mikado.loci.clean.step2.primaryTranscripts.gff3` | A preencher |
| VCF Dataset 2 | `hipstr_trf_v2_filtered.vcf` | A preencher |
| VCF Dataset 3 | `hipstr_post_dumpstr_filtered_trf.vcf` | A preencher |

Os links devem apontar para uma fonte estável e, quando disponível, incluir accession, DOI ou identificador equivalente. Registre também o checksum dos arquivos para permitir a conferência da versão utilizada no artigo.

Os caminhos locais usados no notebook podem ser ajustados para a organização da máquina de execução, mas os nomes dos arquivos devem permanecer consistentes com esta tabela ou ser alterados nas etapas correspondentes do pipeline.
