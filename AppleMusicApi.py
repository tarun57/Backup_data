import applemusicpy

secret_key=''
key_id = '34MTF92235'
team_id = 'N9DZ7SVRB9'

am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
results = am.search('travis scott', types=['albums'], limit=5)

for item in results['results']['albums']['data']:
    print(item['attributes']['name'])
