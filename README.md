# pGlycoQuant_source_code

### Version: pGlycoQuant_V1.1
### Release Date: 2021.08.31

## Computer configuration
RAM: 16G or higher is recommended
ROM: for one raw data (1G) 5G or higher is recommended
OS: Windows10 or higher
Other: MSFileReader 3.0 Sp1 or higher is needed

## Description
At present, pFind, pGlyco, Byonic and MSFragger software glycosylation identification results can be used for quantification by pGlycoQuant.
![image](https://user-images.githubusercontent.com/29300776/142555796-dce0b97b-4e19-46d3-92f0-faf948b459ab.png)

### Notes for running Byonic result
1. It is found that the name of mass spectrum data recorded by Byonic software is inconsistent with the original data, when running pGlycoQuant in Byonic mode, it should be guaranteed that the name of the mass spectrum data recorded in the Byonic result file is the same as that of the entered mass spectrum data.
2. Byonic glycosylation modification reliable results screening commonly used scores are Score and LogProb, rather than FDR. FDR cannot be modified on the pGlycoQuant interface. To modify B4_THRESHOLD_SCORE_BYONIC and B5_THRESHOLD_PROB_BYONIC in the config file (default: 200 and 2, indicating score≥200 and absolute value of LogProb ≥2).
3. Byonic ini files are required for quantification, in the ./ini/ini_Byonic directory.

### Notes for running MSFragger result
MSFragger ini files are required for quantification, in the ./ini/ini_MSFragger directory.

## Cite us
Weiqian Cao, et. al. pGlycoQuant with a deep residual network for precise and minuscule-missing-value quantitative glycoproteomics enabling the functional exploration of site-specific glycosylation. bioRxiv 2021.11.15.468561.
doi: https://doi.org/10.1101/2021.11.15.468561
![image](https://user-images.githubusercontent.com/29300776/142555844-e7904557-4da4-415c-9cfb-2e3f66965310.png)
