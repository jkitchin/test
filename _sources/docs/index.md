# Installation

You can use regular Markdown files in Jupyter Book. Here we describe how to install the `oaris` package.

```bash
cd <path/to/src/setup.py>
pip install .
```

This should install the `oaris` package and command-line utility.

# CLI usage

To get an RIS entry output to stdout, simply call the `oaris` executable command with a DOI. For example:

    > oaris https://doi.org/10.1021/acscatal.5b00538
    
should output this content in the shell:

```
TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538
ER  -
```

You can pipe that to another command or redirect that to a file. `oaris` only works on one DOI at a time.