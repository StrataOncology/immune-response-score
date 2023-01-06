# immune-response-score

Strata Oncology Immunotherapy Response Score

Transforms normalized expression and TMB values into an immunotherapy response prediction score

Inputs:
- ADAM12 expression
- CD274 (PD-L1) expression
- TOP2A expression
- PDCD1 (PD1) expression
- tumor mutation burden (count of somatic mutations per sequenced megabase)


Outputs:
- immunotherapy response score (IRS); higher values predict increased benefit

Note:
- Expression values should be provided in log base 2 transformed normalized read counts per million; values for each gene should be median centered across a representative reference clinical population
