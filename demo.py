import requests
import os
import platform

urls = ["url1", "url2"]

def download_file(url):
    file_name = os.path.basename(url)
    file_path = os.path.join(os.path.tempdir, file_name)
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    return file_path

for url in urls:
    file_path = download_file(url)
    if platform.system() == 'Windows':
        os.startfile(file_path)
    elif platform.system() == 'Darwin':  # macOS
        os.system('open "{}"'.format(file_path))
    else:  # Linux or other Unix-like systems
        os.system('xdg-open "{}"'.format(file_path))
