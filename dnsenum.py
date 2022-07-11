import dns.resolver
import sys

record_type= ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'PTR']   #types of dns records to be searched

try:
    domainname = sys.argv[1]
except:
    print('Syntax Error: python3 dnsenum.py <domainname>')

for records in record_type:
    try:
        finding = dns.resolver.resolve(domainname, records) #taking records from the list one at a time
        print(f'\n{records} Records')
        print('-' * 75)
        for dns_detail in finding:
            print(dns_detail.to_text())

    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print("The domain {} does not exist".format(domainname))
    except KeyboardInterrupt:
        print('Seems that you want to quit, Good Bye')
        quit()
