# spyse.py

Python API wrapper for the tools hosted on spyse.com.


"Spyse is a developer of complete DAAS (Data-As-A-Service) solutions for Internet security professionals, corporate and remote system administrators, SSL / TLS encryption certificate providers, data centers and business analysts. All Spyse online solutions are represented by thematic services that have a single platform for collecting, processing and aggregating information."
\- spyse.com

Supports the following APIs:
- [DNStable](https://dnstable.com)
- [FindSubdomains](https://findsubdomains.com)
- [CertDB](https://certdb.com)
- [ASlookup](https://aslookup.com)
- [PortMap](https://portmap.com)
- [DomainsDB](https://domainsdb.org)


#### NOTE: This API is currently under active development.

## Examples

#### Without API Key
```python
from pprint import pprint
from spyse import spyse

s = spyse()
pprint(s.subdomains_aggregate("xbox.com", param="domain"))
```

#### With API Key
```python
from spyse import spyse

s = spyse('API_TOKEN_GOES_HERE')
pprint(s.subdomains_aggregate("xbox.com", param="domain"))
```

#### Search using CIDR
```python
from spyse import spyse
from pprint import pprint

s = spyse()
pprint(s.domains_on_ip("172.217.1.0/24", param="cidr"))
```
