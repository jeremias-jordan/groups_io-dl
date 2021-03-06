import json
import requests
import os
import errno
import argparse

parser = argparse.ArgumentParser(prog="Groups.io-dl", description='Groups.io Downloader')
parser.add_argument('-u','--username', help='username/email', required=True)
parser.add_argument('-p','--password', help='password', required=True)
parser.add_argument('-g', '--group', help="Group Name", required=True)
args = parser.parse_args()

print(args.username)
print(args.password)
print(args.group)
email = args.username
password = args.password
groupname = args.group
group_name = {'group_name' : groupname, 'limit' : 100}

r0 = requests.post('https://groups.io/api/v1/login', data = {'email' : email, 'password' : password})
groupscookie = r0.cookies

def dl_folder (path):

    print("Downloading folder " + path)
    group_name['path'] = path
    t = requests.get('https://groups.io/api/v1/getfiledirectory', params=group_name, cookies=groupscookie)
    t = t.json()
    if t["data"]:
        for entry in t["data"]:
            if entry["type"] == "file_type_dir":
                pa = entry["name"]
                dl_folder('/'.join([path, pa]))
            elif entry["download_url"]:
                dl_file(entry["download_url"], entry["path"], entry["name"])

def dl_file(dl_url, path, name): 
    
    print("Downloading file " +  name + " ...")
    path_to_file = '/'.join(['.', path, name])
    gr = group_name
    gr['path'] = path

    d = requests.get(dl_url, cookies=groupscookie)

    if not os.path.exists(os.path.dirname(path_to_file)):
        try:
            os.makedirs(os.path.dirname(path_to_file))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(path_to_file, "w") as f:
        f.write(d.content)

dl_folder("")
