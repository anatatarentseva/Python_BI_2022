def read_file(input_fastq):
    with open(input_fastq) as file:
        content = file.readlines()
    reads = []
    for i in range(0, len(content) - 3, 4):
        reads.append(list(content[i:i + 4]))
    return reads

def filter_by_gc(read, gc_bounds):
    if len(gc_bounds) == 1:
        gc_bounds = (0, gc_bounds)
    return gc_bounds[0] <= (sum([1 for c in read if c in 'GC']) * 100) / len(read) <= gc_bounds[1]
    
def filter_by_quality(read, quality_threshold):
    return 100*(1 - 10**(-(sum([ord(r) - ord('!') for r in read]) / len(read))/10)) >= quality_threshold

def filter_by_length(read, length_bounds):
    if len(length_bounds) == 1:
        length_bounds = (0, length_bounds)
    return length_bounds[0] <= len(read) <= length_bounds[1]

def write_file(output_file, content):
    file = open(output_file, "w")
    file.writelines(content)
    file.close()

def main(input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0, save_filtered = False):
    reads = read_file(input_fastq)
    passed, failed = '', ''
    for read in reads:
        if filter_by_gc(read[1], gc_bounds) and filter_by_quality(read[3], quality_threshold) and filter_by_length(read[0], length_bounds):
            passed += ''.join(read)
        elif save_filtered:
            failed += ''.join(read)
    write_file(output_file_prefix + '_passed.fastq', passed)
    if save_filtered:
        write_file(output_file_prefix + '_failed.fastq', failed)