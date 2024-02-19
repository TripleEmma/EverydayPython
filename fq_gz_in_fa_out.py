#! /usr/bin/python
'''
as a reminder how to read in fq.gz and output as fa file;
in this particular example, extract the first 16bp bases which is the UMI sequence
'''

import gzip
def readseq(fqfile, output):
    f_out = open(output, 'w')

    with gzip.open(fqfile, 'r') as f:
        line = f.readline().decode('utf-8').lstrip('@')
        while line:
            f_out.write('>' + line)
            seq = f.readline().decode('utf-8')[:16]
            f_out.write(seq + '\n')
            f.readline()
            f.readline()
            line = f.readline().decode('utf-8').lstrip('@')
    f_out.close()

if __name__ == '__main__':
    import sys
    fqfile, output = sys.argv[1:]
    readseq(fqfile, output)
