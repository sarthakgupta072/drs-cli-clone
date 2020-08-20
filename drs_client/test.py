


# File only for testing. Will be removed in the future commits

from requests.api import delete
from drs_client.client import DRSClient
import json

client = DRSClient(host="http://0.0.0.0")
# print(client.delete_object('t0ltnK'))
# print(client.get_object("t0ltnK"))
# print(client.get_access_url("t0ltnK", "rsn.dn"))
print(client.post_object(object_data={
  "created_time": "2019-05-20T00:12:34-07:00",
  "updated_time": "2019-04-24T05:23:43-06:00",
  "version": "1",
  "size": 5,
  "mime_type": "",
  "checksums": [
    {
      "checksum": "18c2f5517e4ddc02cd57f6c7554b8e88",
      "type": "md5"
    }
  ],
  "access_methods": [
    {
      "type": "ftp",
      "access_url": {
        "url": "drs://ftp.ensembl.org/pub/release-81/bed/ensembl-compara/11_teleost_fish.gerp_constrained_eleme",
        "headers":  [
          "None"
        ]
      }
    }
  ]
}))
    
