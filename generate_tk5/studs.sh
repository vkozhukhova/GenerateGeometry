#!/bin/bash
# щас наваяем... наверное...
file="/home/varvara/Latex/generate_tk5/students.txt"
while read line
do
a="`echo $line|sed 'y/абвгдзийклмнопрстуфхыэеАБВГДЗИЙКЛМНОПРСТУФХЫЭЕ/abvgdzijklmnoprstufhyeeABVGDZIJKLMNOPRSTUFHYEE/'|sed 's/[ьъ]//g; s/ё/yo/g; s/Ё/Yo/g; s/ж/zh/g; s/Ж/Zh/g; s/ц/ts/g; s/Ц/Ts/g; s/ч/ch/g; s/Ч/Ch/g; s/ш/sh/g; s/Ш/Sh/g; s/щ/sch/g; s/Щ/Sch/g; s/ю/yu/g; s/Ю/Yu/g; s/я/ya/; s/Я/Ya/; s/ /_/g'`"
echo "$line" >> "$a".txt
pdflatex -jobname="$a" '\def\teachers{}\input{geom_tk5}'
/usr/lib/sagemath/sage "$a".sagetex.sage
pdflatex -jobname="$a" '\def\teachers{}\input{geom_tk5}'
pdflatex -jobname="$a" -output-directory=/home/varvara/Latex/generate_tk5/stud '\input{geom_tk5}'
done < $file
find . -type f ! -name "*.pdf" ! -name "*.sty" ! -name "geom_tk5*" ! -name "students.txt" ! -name "*.sh" -delete
find . -name '*sage-plots*' ! -name "*geom_tk5*" -exec rm -rf {} +
