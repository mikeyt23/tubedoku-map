import json

with open('stations.json', 'r', encoding='utf-8') as f:
    stations = json.load(f)

compact = []
for s in stations:
    compact.append({
        'n': s['name'],
        'z': s['zone'] or '1',
        'l': s['lines'],
        'lat': round(s['lat'], 5) if s['lat'] else 0,
        'lon': round(s['lon'], 5) if s['lon'] else 0,
        'id': s['id']
    })

stations_json = json.dumps(compact, separators=(',', ':'))

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

output = template.replace('__STATIONS_JSON__', stations_json)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Generated index.html successfully! Size: {len(output)} bytes")
