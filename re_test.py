__author__ = 'X'
import re

data = '1abc123edda 123sdf235gd09gd zffgp4'

print(re.findall(r'(?:abc)|(?:sdf)',data))
print(re.findall(r'zff',data))

us_presidents = ["Adams", "Bush", "Clinton", "Obama", "Harrison", "Taft", "Bush", "Adams", "Wilson", "Roosevelt", "Roosevelt"]

us_president_counts = {}
print(us_president_counts)
for president in us_presidents:
    if president in us_president_counts:
        us_president_counts[president] = us_president_counts[president] + 1

    else:
        us_president_counts[president] = 1
print(us_president_counts)


data1 = 'img src=\'https://3d.media.tumblr.com/a1b8d9cd5750f97dec594bf6ab0a193a/tumblr_nx2etx9pQ81ug7mq1o1_500.gif'
print(re.findall(r'img src=\'(https://3\d.{,120}\.gif)',data1))
