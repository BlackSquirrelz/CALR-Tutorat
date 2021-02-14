from CorpusProcessing import pre_processing as pp


# reading any file
def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()
    return content


if __name__ == '__main__':
    path = "Data/RAW/test.txt"
    text = read_file(path)



