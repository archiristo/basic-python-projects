import numpy as np
import re

data = open("data.txt")
read = data.read()
print(read)

maillist = re.findall("\S+@\S+", read)
print(maillist)