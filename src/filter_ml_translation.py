# -*- coding: utf-8 -

# import tldextract
import validators
from tld import get_fld
from tld.utils import update_tld_names

# Update the list of TLD names
update_tld_names()

f = open("./data/ml-translation_raw.txt", "r")
other_regex_f = open("./data/ml-translation_match_patterns_raw.txt", "r")

filter_domain_list = []
for line in f.readlines():
    #print(line)
    line = line.strip()
    if len(line) > 0 and not line.startswith("!#"):
        if line.startswith("*://*."):
            line = line.replace("*://*.", "")
        if line.startswith("*://"):
            line = line.replace("*://", "")
        if line.endswith('/*'):
            line = line.replace("/*", "")
        print("->   " + line)
        if validators.domain(line):
            fld = get_fld(line, fix_protocol=True)
            filter_domain_list.append("*://*." + fld + "/*")

content = sorted(set(filter_domain_list))
print("total count: {}".format(len(content)))
raw_content = "\n".join(content)
raw_other_regex = "".join(other_regex_f.readlines())

with open("ml-translation_v1.txt", "w") as f:
    f.truncate(0)
    f.write(raw_other_regex)
    f.write("\n!# domain list\n")
    f.write(raw_content)
    f.close()
