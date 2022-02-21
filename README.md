Certbot DNS Auth Plugin
===============================================================================================================

Support Alibabacloud And Name.com

## Edit `config.ini`
```
[alibabadns]
endpoint = XXXXXXXXXX
access_key_id = XXXXXXXX
access_key_secret = XXXXXXXXXX
[namecomdns]
username = XXXXXXXXXX
token = XXXXXXXXXX
```
## Edit `/etc/letsencrypt/renewal/[domain].conf`

Append `manual_auth_hook` and `manual_cleanup_hook`
```
[renewalparams]
authenticator = manual
account = xxxxxxxxxxxxxxxxxxx
pref_challs = dns-01,
manual_public_ip_logging_ok = True
server = https://acme-v02.api.letsencrypt.org/directory
manual_auth_hook    = python /path/main.py [alibabadns|namecomdns] --auth
manual_cleanup_hook = python /path/main.py [alibabadns|namecomdns] --cleanup
```

## How to run
```shell
certbot renew
```