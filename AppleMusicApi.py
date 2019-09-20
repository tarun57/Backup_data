import applemusicpy
import jwt

secret_key='-----BEGIN PRIVATE KEY-----\
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgIICe4VRtABygJZsP+VUIHvIUh0VcL3FJlV8hS7d6ytKgCgYIKoZIzj0DAQehRANCAAT2Q6bc+l4lF+kGrLaFAGLGo8NZGAIIRdejGIGQ/Eh8rBnCcI7LQ+MpmLl/AaFzxT+67QVDZrqa1zaEWARq/5V9\
-----END PRIVATE KEY-----'
key_id = '34MTF92235'
team_id = 'N9DZ7SVRB9'

am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
results = am.search('travis scott', types=['albums'], limit=5)

for item in results['results']['albums']['data']:
    print(item['attributes']['name'])
