import os
import sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

default_basepath = "/"

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./notes"

# template_path = "./template.html"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Setup public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Generating static assets")
    copy_files_recursive(dir_path_static, dir_path_public)

    # print("Generating pages...")
    # generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()
