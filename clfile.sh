#!/usr/bin/python

cd /home/user01/ncas-isc/shell/acsoe/eae-97/macehead

for i in *
do 
echo ==$i==
tail -1 $i
done
tail -1 kwesi/ 
tail -1 kwesi/  2> era-log.txt
cat era-log.txt
