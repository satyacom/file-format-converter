import json

import glob

import uuid

import os

import pandas as pd
import logging

#folder paths are hard coded

#schemas.json path is also hard coded

#modularization with reusability

def get_columns(ds):

    with open('data/retail_db/schemas.json') as fp:

        schemas = json.load(fp)

    try:

        schema = schemas.get(ds)

        if not schema:

            raise KeyError

        cols = sorted(schema, key=lambda s: s['column_position'])

        columns = [col['column_name'] for col in cols]

        return columns

    except KeyError:

        print(f'schema not found {ds}')

        return

def main():
    logging.basicConfig(
        filename=  'logs/ffc.log',
        level=logging.INFO,
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p'
    )

    set_base_dir =os.environ['SRC_BASE_DIR']
    tgt_base_dir = os.environ['TGT_BASE_DIR']
    
    for path in glob.glob(f'{ set_base_dir}/*'):

        if os.path.isdir(path):

            ds = os.path.split(path)[1]

            for file in glob.glob(f'{path}/part*'):

                df = pd.read_csv(file, names=get_columns(ds))

                os.makedirs(f'{ tgt_base_dir}/{ds}', exist_ok=True)

                df.to_json(

                    f'{ tgt_base_dir}/{ds}/part-{str(uuid.uuid1())}.json',

                    orient='records',

                    lines=True

                )

                logging.info(f'Number of records processed for {os.path.split(file)[1]} in {ds} is {df.shape[0]}')

 

 

if __name__ == '__main__':

    main()