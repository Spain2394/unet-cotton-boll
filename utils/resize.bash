shopt -s nullglob
for image in ./tests_transformed/*.jpg; do
	mogrify -resize 1567X361 "${image}"
done
