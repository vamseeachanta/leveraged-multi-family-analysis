"""Leveraged Multi Family Real Estate Analysis.

Usage:
------

python -m lmfa 'multifamily_2.yaml', 'multifamily_4.yaml'


Contact:
--------

More information is available at:

- https://pypi.org/project/leveraged-multi-family-analysis/
- https://github.com/vamseeachanta/leveraged-multi-family-analysis


Version:
--------

- leveraged-multi-family-analysis v0.1.4
"""
import os
import pathlib
from lmfa import multifamily
from lmfa.utilities import get_config_files


def main() -> None:
    parent_path = pathlib.Path(__file__).resolve().parent
    config_files = get_config_files()

    config_files = [
        os.path.join(parent_path, config_file) for config_file in config_files
    ]

    multifamily.run_analysis()


if __name__ == "__main__":
    main()
