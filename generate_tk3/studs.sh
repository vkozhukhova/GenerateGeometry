#!/bin/bash
# щас наваяем... наверное...
file="/home/varvara/Latex/generate_tk3/students.txt"
while read line
do
a="`echo $line|sed 'y/абвгдзийклмнопрстуфхыэеАБВГДЗИЙКЛМНОПРСТУФХЫЭЕ/abvgdzijklmnoprstufhyeeABVGDZIJKLMNOPRSTUFHYEE/'|sed 's/[ьъ]//g; s/ё/yo/g; s/Ё/Yo/g; s/ж/zh/g; s/Ж/Zh/g; s/ц/ts/g; s/Ц/Ts/g; s/ч/ch/g; s/Ч/Ch/g; s/ш/sh/g; s/Ш/Sh/g; s/щ/sch/g; s/Щ/Sch/g; s/ю/yu/g; s/Ю/Yu/g; s/я/ya/; s/Я/Ya/; s/ /_/g'`"
echo "$line" >> "$a".txt
pdflatex -jobname="$a" '\def\teachers{}\input{geom_tk3}'
/usr/lib/sagemath/sage "$a".sagetex.sage
pdflatex -jobname="$a" '\def\teachers{}\input{geom_tk3}'
pdflatex -jobname="$a" -output-directory=/home/varvara/Latex/generate_tk3/stud '\input{geom_tk3}'
done < $file
find . -type f ! -name "*.pdf" ! -name "*.sty" ! -name "geom_tk3*" ! -name "students.txt" ! -name "*.sh" -delete
find . -name '*sage-plots*' ! -name "*geom_tk3*" -exec rm -rf {} +
# найди все папки кроме stud и удали вместе с содержимым
