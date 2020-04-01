#PBS -S /bin/bash
#PBS -N unet_pytorch_cmon
#PBS -q gpu_q
#PBS -l nodes=1:ppn=2:gpus=2:K40:default
#PBS -l walltime=48:00:00
#PBS -l mem=20gb
#PBS -M avs81684@uga.edu 
#PBS -m abe

cd /scratch/avs81684/pytorch_unet_cmon

# dependencies
#ml CUDA/10.1.243
#ml CUDA/10.1.243-GCC-8.3.0
ml tensorflow/1.14-fosscuda-2018b-Python-3.6.6
ml tqdm/4.44.1-fosscuda-2018b-Python-3.6.6
ml torchvision/0.5.0-fosscuda-2018b-Python-3.6.6

echo "Job ID: $PBS_JOBID"
echo "Queue:  $PBS_QUEUE"
echo "Cores:  $PBS_NP"
echo "Nodes:  $(cat $PBS_NODEFILE | sort -u | tr '\n' ' ')"

# train after interactive test
# python3 train.py --load model.pth --epochs 50 > output_${PBS_JOBID}.log

# interactive test
# python3 predict.py --input /scratch/avs81684/Pytorch-UNet/data/train/plotid_101.png --output ./test_output_cotton.jpg > output_${PBS_JOBID}.log

# python3 predict.py --input ./data/train_cotton/0001.jpg --output ./cotton.jpg --model ./checkpoints/CP_epoch\{epoch\ +\ 1\}.pth 
python3 train.py -epochs 30 --validation 20 --scale 1 > ./logs/output_${PBS_JOBID}.log

