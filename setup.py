from setuptools import setup, find_packages

setup(
    name = "python-escpos-jp",
    version = "0.1",
    author = "iakyi",
    author_email = "iakyi@yahoo.co.jp",
    url = "https://github.com/iakyi/python-escpos-jp",
    download_url = "http://github.com/iakyi/python-escpos-jp/archive/master.zip",
    install_requires= ["python-escpos",],
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
