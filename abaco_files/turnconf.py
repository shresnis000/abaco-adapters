import json

# Opening JSON file
with open('config-local.json', 'r') as f:
  data = json.load(f)
  
# returns JSON object as 
data2= data
p=list(data.keys())
n=0
for i in data2:
    k=f"{{globalconfig['{p[n]}']}}"
    data2[i]=f'{{{k}}}'
    n=n+1
    
with open('config.json', 'w') as json_file:
  json.dump(data2, json_file, indent=4)
