from readers.file_reader import FileReader
import xml.etree.ElementTree as ET


class XmlFileReader(FileReader):
    def read(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        return [elem for elem in root.findall('information')]
