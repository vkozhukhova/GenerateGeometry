#!/bin/bash
# щас наваяем... наверное...
cd /home/varvara/Latex/generate_pk1/
file="/home/varvara/Latex/generate_pk1/students.txt"
COUNTER=1
while read line
do
#a="`echo $line|sed 'y/абвгдзийклмнопрстуфхыэеАБВГДЗИЙКЛМНОПРСТУФХЫЭЕ/abvgdzijklmnoprstufhyeeABVGDZIJKLMNOPRSTUFHYEE/'|sed 's/[ьъ]//g; s/ё/yo/g; s/Ё/Yo/g; s/ж/zh/g; s/Ж/Zh/g; s/ц/ts/g; s/Ц/Ts/g; s/ч/ch/g; s/Ч/Ch/g; s/ш/sh/g; s/Ш/Sh/g; s/щ/sch/g; s/Щ/Sch/g; s/ю/yu/g; s/Ю/Yu/g; s/я/ya/; s/Я/Ya/; s/ /_/g'`"
#echo "$line" >> "$a".txt
b=$(( $RANDOM + 1 ))
echo "$COUNTER" >> "$COUNTER".txt
pdflatex -jobname="$COUNTER" '\def\teachers{}\def\myvar{'`echo $b`'}\input{geom_pk1}'
/usr/lib/sagemath/sage "$COUNTER".sagetex.sage
pdflatex -jobname="$COUNTER" '\def\teachers{}\def\myvar{'`echo $b`'}\input{geom_pk1}'
pdflatex -jobname="$COUNTER" -output-directory=/home/varvara/Latex/generate_pk1/stud '\def\myvar{'`echo $b`'}\input{geom_pk1}'
COUNTER=$((COUNTER + 1))
done < $file
find . -type f ! -name "*.pdf" ! -name "*.sty" ! -name "geom_pk1*" ! -name "students.txt" ! -name "*.sh" -delete
