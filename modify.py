import json

# Načti JSON soubor
with open('version.json', 'r') as file:
    data = json.load(file)

    # Změň hodnotu
    data['version'] = '2.0.0'

# Ulož zpět do JSON souboru
with open('version.json', 'w') as file:
    json.dump(data, file, indent=2)