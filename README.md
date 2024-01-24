## NAME

yaml2data - Generate multiple data files from a single YAML file

## SYNOPSIS

    python yaml2data.py [-h] file

## DESCRIPTION

    Generate data files in multiple formats
    using a single YAML file encoded in UTF-8.

## OPTIONS

    file FILE
        YAML file encoded in UTF-8

    -h, --help
        Help message

## INPUT FILE SYNTAX

    Refer to the enclosed file "sample.yaml".

## EXAMPLES

    python yaml2data.py sample.yaml

## LIST OF THIRD-PARTY PYTHON PACKAGES

| Package    | Version | Repository |
|------------|---------|------------|
| pyyaml     | 6.0.1   | anaconda   |
| openpyxl   | 3.0.10  | anaconda   |
| jinja2     | 3.1.2   | anaconda   |
| matplotlib | 3.8.0   | anaconda   |
| tabulate   | 0.9.0   | anaconda   |
| pandas     | 2.1.4   | anaconda   |

**Conda configuration steps**

1. conda create -n yaml2data python=3.11.7 pyyaml=6.0.1 openpyxl=3.0.10 jinja2=3.1.2 tabulate=0.9.0 pandas=2.1.4
1. conda activate yaml2data

## SEE ALSO

[datagen - Generate data in multiple formats](https://github.com/jangcom/datagen)

## AUTHOR

Jaewoong Jang \<jangj@korea.ac.kr\>

## COPYRIGHT

Copyright (c) 2021-2024 Jaewoong Jang

## LICENSE

This software is available under the MIT license;
the license information is found in 'LICENSE'.
