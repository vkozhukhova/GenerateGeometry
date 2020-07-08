#!/bin/bash
# щас наваяем... наверное...
cd /home/varvara/Latex/geom_exam/
find examtry1.pdf bilety.pdf -delete
n=6
for ((COUNTER=1; COUNTER < $n; COUNTER++))
do
firstseed=$(( $RANDOM + 1 ))
secondseed=$(( $RANDOM + 1 ))
xelatex -jobname="$COUNTER" '\def\examno{'`echo $COUNTER`'}\def\firstseed{'`echo $firstseed`'}\def\secondseed{'`echo $secondseed`'}\input{examtry1}'
/usr/lib/sagemath/sage "$COUNTER".sagetex.sage
xelatex -jobname="$COUNTER" '\def\examno{'`echo $COUNTER`'}\def\firstseed{'`echo $firstseed`'}\def\secondseed{'`echo $secondseed`'}\input{examtry1}'
done
find . -type f ! -name "*.pdf" ! -name "*.sty" ! -name "examtry1*" ! -name "geom_vectors*" ! -name "bilety*" ! -name "geom_theory*" ! -name "students.txt" ! -name "*.sh" -delete
pdftk *.pdf cat output bilety.pdf
#COUNTER=1
#while read line
#do
#COUNTER=$((COUNTER + 1))
#done < $file



