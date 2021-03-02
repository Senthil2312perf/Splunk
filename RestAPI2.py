import requests
import json
import time
import csv

data = {
  'id': 'mysearch_02151949',
  'max_count': '50000',
  'status_buckets': '300',
  'search':'search index=_internal sourcetype=splunkd | stats count by event_message'
}

response = requests.post('https://localhost:8089/servicesNS/admin/search/search/jobs', data=data, verify=False, auth=('admin', 'Bnymellon123'))
print(response.text)

data = {'output_mode': 'json'}
time.sleep(10)

splunk_base_url = 'https://localhost:8089/servicesNS/admin/search/search/jobs/mysearch_02151949/results'
splunk_base_results = requests.get(splunk_base_url, data=data, verify=False, auth=('admin', 'Bnymellon123'))
splunk_base_data = splunk_base_results.json()

print(splunk_base_data)
for data in splunk_base_data['results']:
  print(data)


with open ("output.csv", "w") as f:
  csvfile = csv.writer(f,lineterminator='\n')
  csvfile.writerow(["event_message","count"])
  for item in splunk_base_data['results']:
    csvfile.writerow([item['event_message'],item['count']])
