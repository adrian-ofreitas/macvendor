# Get Mac Vendor Info

## OSINT - This is a simple Python script to search mac vendor info


<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a> 
</p>

## Installation

```console
# clone the repo
$ git clone https://github.com/adrian-ofreitas/macvendor.git

# change the working directory to sherlock
$ cd macvendor/

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```console
$ python3 macvendor --help
usage: python main.py [-o ORG] [-d DATE]

OSINT - This is a simple Python script to search payment of civil servant.

options:
  -h, --help            show this help message and exit
  -v, --version         Version
  -s MAC, --search MAC     Mac Address to Search to search
  
```

To search file with payments of June:
```
python3 macvendor --search AA:BB:CC:DD:EE:FF
```