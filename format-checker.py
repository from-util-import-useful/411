import re
from sys import exit


def tprint(checker):
    print "Here is what I see."
    print("{0:20} {1:20}".format("Key", "Value"))
    padding = ' ' * 21
    for k, v in sorted(checker.items()):
        nv = ('\n' + padding).join(v.split('\n'))
        print ("{0:20} {1:20}\n".format(k, nv))

with open("./mp1_submission.txt", "r") as f:
    res = [i.strip() for i in f.readlines()]
keep = re.compile(r"^\s*[^#]")
useful = "\n".join(filter(keep.match, res))
key_vals = [i.strip() for i in useful.split('"|"') if len(i.strip()) > 0]
keys = [re.sub(r"\s*=$", "", i) for i in key_vals[::2]]
vals = key_vals[1::2]
actual_keys = {'TASK1_WEBSERVER', 'TASK2_DBNAME', 'TASK2_HOSTNAME', 'TASK2_PASSWORD', 'TASK2_USER', 'TASK3_SQL', 'TASK4_SQL', 'TASK5_SQL', 'TASK6_SQL'}
checker = dict(zip(keys, vals))

if actual_keys != set(keys):
    print "Your format is messed up!"
    tprint(checker)
    exit(1)

if "demo.php" in checker["TASK1_WEBSERVER"]:
    print "You should not have demo.php in TASK1_WEBSERVER"
    tprint(checker)
    exit(1)

print "WIN! Your formatting seems okay!"
tprint(checker)
exit(0)
