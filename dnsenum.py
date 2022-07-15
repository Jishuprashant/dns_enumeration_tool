import dns.resolver
import sys
from datetime import datetime as dt

record_type= ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'PTR']   #types of dns records to be searched

try:
    domainname = sys.argv[1]
except:
    print('\nOops, Syntax Error!!')
    print('-' * 75)
    print('Syntax Error: python3 dnsenum.py <domainname>')
    
#Adding Banner
print("\n")
print("*" * 50)
print("Checking for DNS Records of: www."+sys.argv[1])
print("Process started at: "+str(dt.now()))
print("*" * 50)
#Banner ends here
    
    
for records in record_type:
    try:
        details = dns.resolver.resolve(domainname, records) #taking records from the list one at a time
        print(f'\n{records} Records')
        print('-' * 75)
        for dns_detail in details:
            print(dns_detail.to_text())

    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print('\n')
        print('-' * 75)
        print("Oo, the domain {} does not exist".format(domainname))
        print('-' * 75)
        quit()
    except NameError:
        quit()
    except KeyboardInterrupt:
        print('Seems that you want to quit, Good Bye')
        quit()
