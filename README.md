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

## DEPENDENCIES

- PyYAML v5.1.2 or higher
- pandas v1.0.0 or higher
- tabulate >=v0.8.9 or higher

## SEE ALSO

[datagen - Generate data in multiple formats](https://github.com/jangcom/datagen)

## AUTHOR

Jaewoong Jang \<jangj@korea.ac.kr\>

## COPYRIGHT

Copyright (c) 2021 Jaewoong Jang

## LICENSE

This software is available under the MIT license;
the license information is found in 'LICENSE'.
