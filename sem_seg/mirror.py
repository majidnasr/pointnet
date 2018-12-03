import os
import glob
import sys
import numpy as np
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)

data_dir = os.path.join(ROOT_DIR, 'data')
mirrored_dir = os.path.join(data_dir, 'mirrored')
if not os.path.exists(mirrored_dir):
    os.mkdir(mirrored_dir)
anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/anno_paths.txt'))]


for anno_path in anno_paths:
    print(anno_path)
    elements = anno_path.split('/')
    area = os.path.join(mirrored_dir+'/'+elements[-3])
    if not os.path.exists(area):
        os.mkdir(area)
    part = os.path.join(area+'/'+elements[-2])
    if not os.path.exists(part):
        os.mkdir(part)
    output_dir = os.path.join(part+'/'+'Annotations')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    input = np.loadtxt(data_dir+'/'+'Stanford3dDataset_v1.2_Aligned_Version'+'/'+elements[-3]+'/'+elements[-2]+'/'+elements[-2]+'.txt', dtype=np.float, delimiter=' ')
    num=len(input)
    out = input
    for i in range(num):
        out[i,0] = -input[i,0]
    np.savetxt(part+'/'+elements[-2]+'.txt', out, fmt='%.3f %.3f %.3f %d %d %d')
    for f in glob.glob(os.path.join(data_dir, 'Stanford3dDataset_v1.2_Aligned_Version', anno_path, '*.txt')):
        out_filename = os.path.basename(f)
        input = np.loadtxt(f, dtype=np.float, delimiter=' ')
        print (f)
        num=len(input)
        print (num)
        out = input
        for i in range(num):
            out[i,0] = -input[i,0]
        np.savetxt(output_dir+'/'+out_filename, out, fmt='%.3f %.3f %.3f %d %d %d')
