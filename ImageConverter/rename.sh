#renaming files in the dataset
a=1
for i in *.png; do
  new=$(printf "%d.png" "$a")
  mv -i -- "$i" "$new"
  let a=a+1
done
