from tqdm import tqdm
import numpy as np
import math
import sys
import os
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from piqa.lpips import LPIPS
from piqa.ssim import MS_SSIM
import pyiqa


# FID
def fid(dist_dir, ref_dir):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    fid_metric = pyiqa.create_metric('fid', device=device)
    fid_score = fid_metric(dist_dir, ref_dir)
    
    return fid_score

# LPIPS and MS-SSIM
def rmetrics(a,b):
    a = np.asarray(a)
    b = np.asarray(b)
    a, b = torch.from_numpy(a).float().cpu(), torch.from_numpy(b).float().cpu()
    a, b = a.permute(2,0,1).unsqueeze(0), b.permute(2,0,1).unsqueeze(0)
    
    if a.shape[2] != b.shape[2] or a.shape[3] != b.shape[3]:
        a = nn.functional.interpolate(a, size=(b.shape[2], b.shape[3]))
        
    #ssim
    ms_ssim = MS_SSIM()(a, b).item()
    #lpips
    a = a.to(torch.device('cuda'))
    b = b.to(torch.device('cuda'))
    lpips_model = LPIPS(network="vgg").to(torch.device('cuda'))
    lpips = lpips_model(a, b).item()
    
    return ms_ssim, lpips


def main():
    result_paths = sys.argv[1]
    reference_paths = sys.argv[2]
    fid_score = fid(result_paths, reference_paths)
    sumssim, sumlpips = 0., 0.
    N=0
    for file in tqdm(os.listdir(result_paths)):
        result_path = os.path.join(result_paths, file)
        reference_path = os.path.join(reference_paths, file)
        
        #corrected image
        corrected = plt.imread(result_path)
        reference = plt.imread(reference_path)

        ms_ssim, lpips = rmetrics(corrected, reference)

        sumssim += ms_ssim
        sumlpips += lpips
        N +=1

        
    mssim = sumssim/N
    mlpips = sumlpips/N
    
    print('Total FID', fid_score)
    print('Total MS-SSIM', mssim)
    print('Total LPIPS', mlpips)
    

if __name__ == '__main__':
    main()