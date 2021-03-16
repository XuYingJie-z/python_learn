#!/usr/bin/python

import  numpy as np
import  numpy as np
def get_GC_fastq(bed_file):
    '''
    用来计算read中每一个单位的GC含量，输入文件为fastq文件
    :param bed_file: fastq_file
    :return: GC_percent
    '''

    bed = open(bed_file, 'r')

    lines = bed.readlines()
    ou_list = list(range(2,len(lines), 4))
    matrix = np.zeros((len(lines), len(lines[1])))
    bed.close()
    bed = open(bed_file, 'r')
    line = bed.readline()
    i = 1
    index = 0
    while line:
        if i in ou_list:
            # print(line)
            count = 0
            for h in line:
                if h == 'G' or h == 'C':
                    matrix[index,count] = 1
                else:
                    matrix[index, count] = 0
                count += 1
            index += 1
        i = i + 1
        line = bed.readline()
    bed.close()
    matrix_sum = np.sum(matrix,axis=0)
    GC_percent =  matrix_sum / len(lines)
    return GC_percent
  
def get_GC_fasta(bed_file):
    '''
    用来计算read中每一个单位的GC含量，输入文件为由bed to fasta 转换得到的fasta，每行必须一样长
    这个bed文件可以由m5C或者macs2 callpeak得到的narrow peak，再用R包genomation得到shore
    :param bed_file: fasta_file
    :return: GC_percent
    '''

    bed = open(bed_file, 'r')
    lines = bed.readlines()
    matrix = np.zeros((len(lines), len(lines[1])))
    bed.close()
    bed = open(bed_file, 'r')
    line = bed.readline()
    index = 0
    while line:
        count = 0
        for h in line:
            if h == 'G' or h == 'C':
                matrix[index,count] = 1
            else:
                matrix[index, count] = 0
            count += 1
        index += 1
        line = bed.readline()
    bed.close()
    matrix_sum = np.sum(matrix, axis=0)
    GC_percent = matrix_sum / len(lines)
    return GC_percent


