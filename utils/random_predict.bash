#!/bin/bash
MODEL="./checkpoints/CP_epoch\{epoch\ +\ 1\}.pth"

for filename in ./data/train_cotton/*.jpg; do
        # echo python3 predict.py -i $filename -o "./tests_transformed/_test$i.jpg" --model $MODEL
	time python3 ./predict.py -i $filename -o ./tests_e30/output_$(basename "$filename" .jpg).jpg --model ./checkpoints/CP_epoch\{epoch\ +\ 1\}.pth 
        

        # convert -resize 1567X361 ./tests_transformed/test$i.jpg ./tests_transformed/test$i.jpg
done

cd ./tests_e30
time convert -resize 1567X381 *.jpg

        # convert -resize 1567X361 ./tests_transformed/test$i.jpg ./tests_transformed/test$i.jpg