#!/usr/bin/python3

# Usage examples
#
# ./spysecli.py -target hackerone.com -param domain --subdomains-aggregate
# ./spysecli.py -target "52.14.144.171" -param ip --domains-on-ip
# ./spysecli.py -target "52.14.144.0/24" -param cidr --dns-a

from pprint import pprint
from spyse import spyse
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-target', help="target")
parser.add_argument('-param', help="parameter to use (ip, domain, cidr, url, hash)")
parser.add_argument('-page', help="page")
parser.add_argument('--raw', help="show raw json", action="store_true")
parser.add_argument('--dns-ptr', help="show dns ptr records", action="store_true")
parser.add_argument('--dns-soa', help="show dns soa records", action="store_true")
parser.add_argument('--dns-mx', help="show dns mx records", action="store_true")
parser.add_argument('--dns-aaaa', help="show dns aaaa records", action="store_true")
parser.add_argument('--dns-ns', help="show dns ns records", action="store_true")
parser.add_argument('--dns-a', help="show dns a records", action="store_true")
parser.add_argument('--dns-txt', help="show dns txt records", action="store_true")
parser.add_argument('--domains-with-same-ns', help="show domains with same ns", action="store_true")
parser.add_argument('--domains-using-as-mx', help="show domains using as mx", action="store_true")
parser.add_argument('--domains-on-ip', help="show domains on ip", action="store_true")
parser.add_argument('--subdomains-aggregate', help="show subdomains aggregate", action="store_true")
args = parser.parse_args()

if args.target and args.param:
	if args.page:
		page = args.page
	else:
		page = 1

	target = args.target
	param = args.param

	s = spyse()

	if args.subdomains_aggregate:

		if args.raw:
			print(s.subdomains_aggregate(args.target, param=args.param, page=page))
			sys.exit()

		data = s.subdomains_aggregate(args.target, param=args.param, page=page)['cidr']
		keys = data.keys()

		for key in keys:
			domains = data[key]['results']
			for d in domains:
				domain = d['data']['domains']
				if len(domain) > 1:
					for i in domain:
						print(i)
				else:
					print(domain[0])

	if args.dns_ptr:

		if args.raw:
			print(s.dns_ptr(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_ptr(args.target, param=args.param, page=page)

		for record in data['records']:
			print("PTR RECORD @ {} FROM HOSTNAME {}".format(
				record['ip']['ip'],
				record['hostname']
			))

	if args.dns_soa:
		if args.raw:
			print(s.dns_soa(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_soa(args.target, param=args.param, page=page)

		for record in data['records']:
			print("SOA RECORD @ {} FROM {} WITH SERIAL {}".format(
				record['domain']['domain'],
				record['domain']['ip']['ip'],
				record['serial']
				))

	if args.dns_mx:

		if args.raw:
			print(s.dns_mx(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_mx(args.target, param=args.param, page=page)
		for record in data['records']:
			print("MX RECORD @ {} FROM IP {}".format(
				record['mx_domain']['domain'],
				record['mx_domain']['ip']['ip']
			))

	if args.dns_aaaa:

		if args.raw:
			print(s.dns_aaaa(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_aaaa(args.target, param=args.param, page=page)

		for record in data['records']:
			print("AAAA RECORD @ {} FROM IP {}".format(
				record['domain']['domain'],
				record['ipv6']
			))

	if args.dns_ns:

		if args.raw:
			print(s.dns_ns(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_ns(args.target, param=args.param, page=page)

		for record in data['records']:
			print("NS RECORD @ {} FROM {}".format(
				record['ns_domain']['domain'],
				record['ns_domain']['ip']['ip']
			))

	if args.dns_a:

		if args.raw:
			print(s.dns_a(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_a(args.target, param=args.param, page=page)

		for record in data['records']:
			print("A RECORD @ {} FROM {}".format(
				record['domain']['domain'],
				record['ip']['ip']
			))

	if args.dns_txt:

		if args.raw:
			print(s.dns_txt(args.target, param=args.param, page=page))
			sys.exit()

		data = s.dns_txt(args.target, param=args.param, page=page)
		print("TXT RECORDS FROM {}".format(args.target))
		for record in data['records']:
			print('> ', record['data'])

	if args.domains_with_same_ns:

		if args.raw:
			print(s.domains_with_same_ns(args.target, param=args.param, page=page))
			sys.exit()

		data = s.domains_with_same_ns(args.target, param=args.param, page=page)
		print(data)

	if args.domains_using_as_mx:

		if args.raw:
			print(s.domains_using_as_mx(args.target, param=args.param, page=page))
			sys.exit()

		data = s.domains_using_as_mx(args.target, param=args.param, page=page)

		for record in data['records']:
			print("{} USING SAME MX AS {} ON IP {}".format(
				record['domain'],
				args.target,
				record['ip']['ip']
			))

	if args.domains_on_ip:

		if args.raw:
			print(s.domains_on_ip(args.target, param=args.param, page=page))
			sys.exit()

		data = s.domains_on_ip(args.target, param=args.param, page=page)

		for record in data['records']:
			print(record['domain'])
