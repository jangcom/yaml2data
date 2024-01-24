#!/usr/bin/env python3
"""yaml2data: Generate multiple data files from a single YAML file

Functions
---------
read_argv(desc='')
    Read in sys.argv.
read_yaml(file, is_echo=False)
    Read in a YAML file encoded in UTF-8.
gen_dir(d)
    Create a directory if it does not exist.
rpt_gen(fname, is_sq_bracket=True)
    Report file or directory generation.
mk_data(yml, sep_ext_kwargs=';', sep_key_val='='):
    Generate data files based on a user input file.
"""

import os
import re
import argparse
import yaml
import pandas as pd

__author__ = 'Jaewoong Jang'
__version__ = '1.0.2'
__date__ = '2024-01-23'


def read_argv(desc=''):
    """Read in sys.argv.

    Arguments
    ---------
    desc : str
        The description of argparse.ArgumentParser. The default is ''.

    Returns
    -------
    argparse.Namespace
        The Namespace object of argparse.
    """
    parser = argparse.ArgumentParser(
        description=desc,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        help='YAML file encoded in UTF-8')
    return parser.parse_args()


def read_yaml(file,
              is_echo=False):
    """Read in a YAML file encoded in UTF-8.

    Arguments
    ---------
    file : str
        YAML file to be read in.
    is_echo : bool
        Dump the YAML file content. The default is False.

    Returns
    -------
    yaml_loaded : dict
        YAML file content.
    """
    with open(file, encoding='utf-8') as fh:
        yaml_loaded = yaml.load(fh, Loader=yaml.FullLoader)
    if is_echo:
        print('-' * 70)
        print(f'Content of [{file}]')
        print('-' * 70)
        print(yaml.dump(yaml_loaded, sort_keys=False))
    return yaml_loaded


def gen_dir(d):
    """Create a directory if it does not exist.

    Parameters
    ----------
    d : str
        The name of the directory to be created.

    Returns
    -------
    None.
    """
    if not os.path.exists(d):
        d = re.sub(r'\\', '/', d)  # For consistency
        question = f'The designated directory [{d}] not found. Create (y/n)? '
        while True:
            yn = input(question)
            if not re.search(r'(?i)\b\s*[yn]\s*\b', yn):
                continue
            if re.search(r'(?i)y', yn):
                os.mkdir(d)
                rpt_gen(d)
            break


def rpt_gen(fname,
            is_sq_bracket=True):
    """Report file or directory generation.

    Arguments
    ---------
    fname : str
        A file or directory name to be reported.
    is_sq_bracket : bool
        Enclose the file or directory name with a pair of square brackets.
        The default is True.

    Returns
    -------
    None.
    """
    if is_sq_bracket:
        fname = f'[{fname}]'
    print(f'{fname} generated.')


def mk_data(yml,
            sep_ext_kwargs=';', sep_key_val='='):
    """Generate data files based on a user input file.

    Arguments
    ---------
    yml : dict
        A YAML-generated dict containing data specifications.
    sep_ext_kwargs : str
        A separator for a file extension and pandas keyword args.
        The default is ';'.
    sep_key_val : str
        A separator for pandas keyword args. The default is '='.

    Returns
    -------
    None.
    """
    for active in yml['run']['active_ids']:
        if active not in yml:
            continue
        # Copy the contents of "run" keys to each activate ID.
        for run_keys in yml['run']:
            if run_keys == 'active_ids':
                continue
            # e.g. run_keys == out_path, out_fmts, header, ...
            if run_keys not in yml[active]:  # Enables ID-wise overriding
                yml[active][run_keys] = yml['run'][run_keys]
        # Initialization
        list_of_lists = [[] for _ in yml[active]['header']]
        dict_of_lists = {}  # DataFrame input
        num_header = len(yml[active]['header'])
        # Process the data.
        for line in yml[active]['data']:
            spl = re.split(r'\s*[{}]\s*'.format(yml[active]['sep']), line)
            # Assign NaN to data slots exceeding the number of headings.
            if len(spl) < num_header:
                num_insufficient = num_header - len(spl)
                spl += [None] * num_insufficient
            for i in range(num_header):
                try:
                    spl[i] = float(spl[i])
                except ValueError:
                    spl[i] = spl[i]
                list_of_lists[i].append(spl[i])
        for i, s in enumerate(yml[active]['header']):
            # e.g. (0, 'Name'), (1, 'Nawabari'), (2, 'Age (year)'), ...
            dict_of_lists[s] = list_of_lists[i]
        # DF construction
        df = pd.DataFrame(dict_of_lists)
        # File generation
        yml[active]['out_path'] = os.path.expandvars(yml[active]['out_path'])
        gen_dir(yml[active]['out_path'])
        out_bname_w_path = '{}/{}'.format(yml[active]['out_path'],
                                          yml[active]['out_bname'])
        for fmt, ext_kwargs in yml[active]['out_fmts'].items():
            # spl[0]: File extension
            # spl[1:]: pandas keyword arguments (optional)
            spl = re.split(r'\s*[{}]\s*'.format(sep_ext_kwargs), ext_kwargs)
            out_fname = '{}.{}'.format(out_bname_w_path, spl[0])
            args_dct = {}
            if not yml[active]['ctrls']['is_index']:
                args_dct.update({'index': False})
            if len(spl) >= 2:
                args = []
                for arg in spl[1:]:
                    args += re.split(r'\s*[{}]\s*'.format(sep_key_val), arg)
                args_dct = {args[i]: args[i + 1]
                            for i in range(0, len(args), 2)}
            if fmt == 'markdown':
                if 'encoding' in args_dct:
                    buf = open(out_fname, 'w', encoding=args_dct['encoding'])
                    del args_dct['encoding']
                else:
                    buf = open(out_fname, 'w', encoding='utf-8')  # Default
            else:  # All but to_markdown()
                buf = out_fname
            if (fmt == 'excel'
                    and yml[active]['ctrls']['is_excel_bkg']):
                meth_to_call = getattr(df.style.background_gradient(),
                                       'to_{}'.format(fmt))
            else:
                meth_to_call = getattr(df,
                                       'to_{}'.format(fmt))
            meth_to_call(buf, **args_dct)
            rpt_gen(out_fname)


if __name__ == '__main__':
    argv = read_argv()
    the_yml = read_yaml(argv.file)
    mk_data(the_yml)
