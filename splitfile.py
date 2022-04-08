import pandas as pd

# put the path of the file to split
path_file_to_split = r'example\202009-TC1.txt'

# Number of data per file
number_data_per_file = 100000

reader = pd.read_table(path_file_to_split, header=None, sep='*',
                       chunksize=number_data_per_file, iterator=True, index_col=None)

i = 0
for chunk in reader:
    # Folder that saves the split files
    # Path
    folder_saves_split_files = r'example\splittedfiles'
    # filename
    split_filename = r'\splitfilename'
    # change the file extension
    file_extension = '.sql'
    file_name = folder_saves_split_files + \
        split_filename + str(i) + file_extension
    print('Saving file {} ...'.format(i))
    # Change header name
    spool = 'Spool'
    chunk.columns = [spool]
    # Add a last value to each file, for example commit
    commit = 'COMMIT;'
    chunk.loc[chunk.size*100] = [commit]
    chunk.to_csv(file_name, encoding='utf-8', index=False)
    i += 1
