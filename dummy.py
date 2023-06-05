import pickle as pd

# folderLocation = "db/index/"

#file = "db/chroma-collections.parquet"# 
file = "db/chroma-embeddings.parquet"
full_path = file


def readPKL_file():
    with open(full_path, 'rb') as f:
        data = pd.load(f)
        print(data, "\n")


def readParguetFile():
    import pandas as pd
    df = pd.read_parquet(full_path)
    print(df)
    var_all = vars(df)
    print('x')


def readBinFile():
    import struct

    with open(full_path, 'rb') as f:
        data = f.read()
        # Convert binary data into human-readable format
        human_readable_data = struct.unpack('d' * (len(data) // 8), data)
        print(human_readable_data)


# readParguetFile()
# readPKL_file()
# readBinFile()
readParguetFile()
