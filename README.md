# groups.io-dl

With this tool, you can download groups.io files of a given group. It will download all of the groups folders and files to your current working directory.

**Attention:** 

The folder/subfolder limit is 100 due to the API limits. If you need more, open an issue and i'll try to increase it.

Also note that empty folders will be disregarded.

'''

usage: Groups.io-dl [-h] -u USERNAME -p PASSWORD -g GROUP

Groups.io Downloader

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        username/email
  -p PASSWORD, --password PASSWORD
                        password
  -g GROUP, --group GROUP
                        Group Name

'''