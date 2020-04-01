#!/bin/bash
for filename in ./data/train_cotton/*.jpg; do
    for ((i=0; i<=3; i++)); do
        python3 predict.py -i $filename -o "./tests/$(basename "$filename" .jpg)_test$i.jpg" --model /home/aspai/pytorch_unet_cmon/checkpoints/CP_epoch{epoch\ +\ 1}.pth
    done
done