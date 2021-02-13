import re

class Scrapy:
    def __init__(self, file):
        self.file = file
        self.text = ''
        self.data = dict()
        self.read_file()
        self.format()
        self.present()

    def read_file(self):
        with open(self.file, "r", encoding='utf-8') as f:
            self.text = f.read()  
        f.close()

    def format(self):
        anchors = re.findall(r'<a href="(.*?)">(.*?)</a>', str(self.text))
        for link, txt in anchors:
            link = link[:61]
            self.data[link] = txt

    def present(self):
        for k,v in self.data.items():
            print('{}\n{}\n'.format(k,v))

obj = Scrapy(your_html_filename)




