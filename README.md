## NAME

yaml2data - Generate multiple data files from a single YAML file

## SYNOPSIS

    python yaml2data.py [-h] [--file FILE]

## DESCRIPTION

    Generate data files in multiple formats
    using a single YAML file encoded in UTF-8.

## OPTIONS

    -h, --help
        Help message

    --file FILE, -f FILE
        YAML file encoded in UTF-8 (default: None)

## INPUT FILE SYNTAX

    Refer to the enclosed file "sample.yaml".

## EXAMPLES

    python yaml2data.py -f sample.yaml

## DEPENDENCIES

- PyYAML v5.1.2 or higher
- pandas v0.25.1 or higher

## SEE ALSO

[datagen - Generate data in multiple formats](https://github.com/jangcom/datagen)

## AUTHOR

Jaewoong Jang \<jangj@korea.ac.kr\>

## COPYRIGHT

Copyright (c) 2021 Jaewoong Jang

## LICENSE

This software is available under the MIT license;
the license information is found in 'LICENSE'.
