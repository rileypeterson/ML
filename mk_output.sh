base_dir="/Users/riley/PycharmProjects/rileypeterson.github.io"
chapter="chapter4"
file="exercises"
jupyter nbconvert --NbConvertApp.output_files_dir="$base_dir/assets/images/ml-book/$chapter" --to markdown $chapter/$file.ipynb
mv $chapter/$file.md $base_dir/_projects/ml-book/$chapter/$file.md
# Replace absolute paths to images with relative ones
python -c "f = open('$base_dir/_projects/ml-book/$chapter/$file.md'); o = f.read().replace('![png]($base_dir', '![png]('); f = open('$base_dir/_projects/ml-book/$chapter/$file.md', 'w'); f.write(o); f.close();"