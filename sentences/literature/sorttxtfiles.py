import glob

files=glob.glob('./*.txt')
for file in files:
  #read file and save it in a list
  txtfile = open(file,'r',encoding="utf-8")
  lines = txtfile.read().splitlines()
  txtfile.close()
  lines.sort()
  lines= list(dict.fromkeys(lines))
  txtfile = open(file,'w',encoding="utf-8")
  txtfile.write("\n".join(lines))
  txtfile.close()
print("complete")
