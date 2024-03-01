# main.py

from refactor import refactor_code
from mojo_code import apply_mojo_tactics
import utils

if __name__ == "__main__":
    code_base = utils.load_code_base()
    refactored_code = refactor_code(code_base)
    mojo_code = apply_mojo_tactics(refactored_code)
    utils.save_code(mojo_code)
