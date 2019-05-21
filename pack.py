import re
import os

text = open('./resources/META-INF/plugin.xml').read()
pattern = re.compile(r"<version>(.*)</version>")
version = ""
for m in pattern.finditer(text):
	version = m.group(1)
print(version)
path = "./downloads"
if not os.path.exists(path):
    os.makedirs(path)
os.rename('./AndroidSourceViewer.zip', "%s/AndroidSourceViewer-%s.zip"%(path, version))

