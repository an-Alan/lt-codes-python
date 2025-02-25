#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import argparse
import numpy as np
import core
from encoder import encode
from decoder import decode
import random



def blocks_write(blocks, file, filesize):
    """ Write the given blocks into a file
    """

    count = 0
    for data in blocks[:-1]:
        file.write(data)
        count += len(data)

    # Convert back the bytearray to bytes and shrink back 
    last_bytes = bytes(blocks[-1])
    shrinked_data = last_bytes[:filesize % core.PACKET_SIZE]
    file.write(shrinked_data)

def decode_file(filename, file_blocks_n):

    random.seed(30)

    # Generating symbols (or drops) from the blocks
    file_symbols = []
    with open(filename, 'rb') as output_f:
        data = output_f.read(39)
        while len(data) != 0:
            assert len(data) == 39, f"{len(data)}"
            file_symbols.append(core.Symbol(index=0, degree=0, data=data))
            data = output_f.read(39)

    
        
    #dump file_symbols into a file 'wb' write binary            

    # HERE: Simulating the loss of packets?

    # Recovering the blocks from symbols
    recovered_blocks, recovered_n = decode(file_symbols, blocks_quantity=file_blocks_n)
    
    if core.VERBOSE:
        print(recovered_blocks)
        print("------ Blocks :  \t-----------")
        # print(file_blocks)

    if recovered_n != file_blocks_n:
        print("All blocks are not recovered, we cannot proceed the file writing")
        exit()

    splitted = args.filename.split(".")
    if len(splitted) > 1:
        filename_copy = "".join(splitted[:-1]) + "-copy." + splitted[-1] 
    else:
        filename_copy = args.filename + "-copy"

    # Write down the recovered blocks in a copy 
    with open(filename_copy, "wb") as file_copy:
        blocks_write(recovered_blocks, file_copy, filesize)

    print("Wrote {} bytes in {}".format(os.path.getsize(filename_copy), filename_copy))




#########################################################
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Robust implementation of LT Codes encoding/decoding process.")
    parser.add_argument("filename", help="file path of the file to split in blocks")
    parser.add_argument("--systematic", help="ensure that the k first drops are exactaly the k first blocks (systematic LT Codes)", action="store_true")
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("--x86", help="avoid using np.uint64 for x86-32bits systems", action="store_true")
    parser.add_argument("file_blocks_n", help = "file blocks size", type = int)
    args = parser.parse_args()

    core.NUMPY_TYPE = np.uint32 if args.x86 else core.NUMPY_TYPE
    core.SYSTEMATIC = True if args.systematic else core.SYSTEMATIC 
    core.VERBOSE = True if args.verbose else core.VERBOSE    

    print("Systematic: {}".format(core.SYSTEMATIC))

    filesize = os.path.getsize(args.filename)
    print("Filesize: {} bytes".format(filesize))

    # Splitting the file in blocks & compute drops

    decode_file(args.filename, args.file_blocks_n)
    
    print("Blocks: {}".format(args.file_blocks_n))

