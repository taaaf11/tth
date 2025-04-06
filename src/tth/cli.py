from __future__ import annotations

import argparse

from tth.source import create_doc_from_expression


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="tth",
        description="Creates Word documents with truth tables for specified logical expression."
    )
    add_arg = parser.add_argument
    
    add_arg(
        "exp",
        help="The final expression whose truth table is required."
    )
    add_arg(
        "-f",
        "--file",
        default="truth-table.docx",
        help="Name of the resultant Word document. Defaults to the \"truth-table.docx\"."
    )
    
    return parser.parse_args()


def main():
    arguments = parse_args()
    
    create_doc_from_expression(arguments.exp, arguments.file)
    
    
if __name__ == "__main__":
    main()