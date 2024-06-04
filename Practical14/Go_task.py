import xml.dom.minidom
import matplotlib.pyplot as plt
import xml.sax
from datetime import datetime

#define functions using DOM
def parse_DOM(file_path):
    start_time = datetime.now()
    DOMTree = xml.dom.minidom.parse(file_path)
    collection = DOMTree.documentElement
    namespace = collection.getElementsByTagName('namespace')
    total = {}
    
    for name in namespace:
        name_text = name.firstChild.nodeValue
        if name_text not in total:
            total[name_text] = 1
        else:
            total[name_text] += 1
    
    end_time = datetime.now()
    time_taken = end_time - start_time
    print(f"Time taken to parse XML using DOM: {time_taken}")
    return total

#define functions using SAX
def parse_SAX(file_path):
    start_time = datetime.now()
    namelist = []
    total = {}
    class namespaceHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.currentElement = ''
            self.namespace = ''
    
        def startElement(self, tag, attrs):
            self.currentElement = tag
    
        def characters(self, content):
            if self.currentElement == 'namespace':
                self.namespace += content.strip()
    
        def endElement(self, tag):
            if tag == 'namespace':
                if self.namespace:  
                    namelist.append(self.namespace)  
                    self.namespace = ''  
    
    handler = namespaceHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    
    for name in namelist:
        if name not in total:
            total[name] = 1
        else:
            total[name] += 1
    
    end_time = datetime.now()
    time_taken = end_time - start_time
    print(f"Time taken to parse XML using SAX: {time_taken}")
    return total

#read the file (modifing the pathway is allowed)
file_path = 'D:\IBI_note\IBI1_2023-24\IBI1_2023-24\Practical14\go_obo.xml'
total_DOM = parse_DOM(file_path)
total_SAX = parse_SAX(file_path)

# Plotting the results
plt.figure(figsize=(12, 6)) 
bars = plt.bar(total_DOM.keys(), total_DOM.values(), width=0.35, color="blue")
plt.ylabel('frequencies')
plt.title('The Number of Terms within Each Ontology: DOM')
plt.xticks(rotation=90) 
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
plt.tight_layout()
plt.show()
plt.clf()

plt.figure(figsize=(12, 6)) 
bars = plt.bar(total_SAX.keys(), total_SAX.values(), width=0.35, color="green")
plt.ylabel('frequencies')
plt.title('The Number of Terms within Each Ontology: SAX')
plt.xticks(rotation=90) 
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
plt.tight_layout()
plt.show()
plt.clf()

#Time taken to parse XML using DOM: 0:00:05.937263
#Time taken to parse XML using SAX: 0:00:00.905789
#SAX is quicker to complete the task
