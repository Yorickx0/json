
#edit json
with open("./path", 'w') as json_file:
        json.dump(data, json_file, indent=4)



# read json
with open("./path", 'r') as f:
        data = json.load(f)

