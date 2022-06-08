from ast import arg, parse
from xml.dom.expatbuilder import parseString
from docx import Document
import argparse
from Module import get
from configparser import ConfigParser


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, help="Novel page url")
    args = parser.parse_args()
    doc = Document()
    
    config = ConfigParser()
    config.read('Config/setting.cfg')
    nsp = config['DEFAULT']['nsp']

    fname, doc = get.getNovel(args.url, nsp)
    if fname is None and doc is None :
        print("============ End ============")
    else :
        doc.save(nsp + fname + '.docx')
        print("============ Done ============")