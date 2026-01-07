import urllib.request
import json
import requests
import os

class PaperDL:
  url = "https://fill.papermc.io/v3/projects/paper/versions"
  url_template = "/{}/builds/{}"

  def __init__(self):
    content = urllib.request.urlopen(PaperDL.url)
    self.data = json.loads(content.read())
    self.__get_dl_data()

  def latest_version(self):
    return self.data["versions"][0]["version"]["id"]

  def latest_build_number(self):
    builds = self.data["versions"][0]["builds"]
    return builds[-1]

  def full_url(self):
    v = self.latest_version()
    b = self.latest_build_number()
    return PaperDL.url + PaperDL.url_template.format(v, b)
  
  def __get_dl_data(self):
    content = urllib.request.urlopen(self.full_url())
    self.dl_data = json.loads(content.read())
  
  def get_dl(self):
    name = self.dl_data["downloads"]["server:default"]["name"]
    url = self.dl_data["downloads"]["server:default"]["url"]

    return (url, name)
  
  def download_latest(self, dl_location):
    dl_data = self.get_dl()
    url = dl_data[0]
    filename = dl_data[1]

    print(f"Downloading latest build...")
    with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(os.path.join(dl_location + filename), 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              f.write(chunk)

    print(f"Saved to {filename}")