#!/usr/bin/env python

import polars as pl
from pathlib import Path


def main():
    base_path = Path(__file__).parent
    source_path = base_path / 'source-data.csv'
    districts_path = base_path / 'districts.csv'
    amphures_path = base_path / 'amphures.csv'
    provinces_path = base_path / 'provinces.csv'

    zip_path = base_path / 'zip_code.csv'

    source_df = pl.read_csv(source_path).select([
        pl.col('TA_ID').alias('DISTRICT_CODE'), 'LAT', 'LONG'
    ])
    districts_df = pl.read_csv(districts_path, schema=pl.Schema({
        'DISTRICT_ID': pl.Int32,
        'DISTRICT_CODE': pl.Int32,
        'DISTRICT_NAME': pl.String,
        'DISTRICT_NAME_ENG': pl.String,
        'AMPHUR_ID': pl.Int32,
        'PROVINCE_ID': pl.Int32,
        'GEO_ID': pl.Int32,
    })).select(['DISTRICT_CODE', 'DISTRICT_NAME', 'DISTRICT_NAME_ENG', 'AMPHUR_ID', 'PROVINCE_ID'])
    amphures_df = pl.read_csv(amphures_path, schema=pl.Schema({
        'AMPHUR_ID': pl.Int32,
        'AMPHUR_CODE': pl.Int32,
        'AMPHUR_NAME': pl.String,
        'AMPHUR_NAME_ENG': pl.String,
        'GEO_ID': pl.Int32,
        'PROVINCE_ID': pl.Int32,
    })).select(['AMPHUR_ID', 'AMPHUR_CODE', 'AMPHUR_NAME', 'AMPHUR_NAME_ENG'])
    provinces_df = pl.read_csv(provinces_path, schema=pl.Schema({
        'PROVINCE_ID': pl.Int32,
        'PROVINCE_CODE': pl.Int32,
        'PROVINCE_NAME': pl.String,
        'PROVINCE_NAME_ENG': pl.String,
        'GEO_ID': pl.Int32
    })).select(['PROVINCE_ID', 'PROVINCE_CODE', 'PROVINCE_NAME', 'PROVINCE_NAME_ENG'])
    zip_df = pl.read_csv(zip_path, schema=pl.Schema({
        'ID': pl.Int32,
        'DISTRICT_CODE': pl.Int64,
        'ZIP_CODE': pl.Int32,
    }))

    joined_df = (
        districts_df
        .join(amphures_df, on='AMPHUR_ID')
        .join(provinces_df, on='PROVINCE_ID')
        .join(zip_df, on='DISTRICT_CODE')
        .join(source_df, on='DISTRICT_CODE')
        .select([
            pl.col('DISTRICT_CODE').alias('district_code'),
            pl.col('DISTRICT_NAME').alias('district_th'),
            pl.col('DISTRICT_NAME_ENG').alias('district_en'),
            pl.col('AMPHUR_CODE').alias('amphure_code'),
            pl.col('AMPHUR_NAME').alias('amphure_th'),
            pl.col('AMPHUR_NAME_ENG').alias('amphure_en'),
            pl.col('PROVINCE_CODE').alias('province_code'),
            pl.col('PROVINCE_NAME').alias('province_th'),
            pl.col('PROVINCE_NAME_ENG').alias('province_en'),
            pl.col('ZIP_CODE').alias('zip_code'),
            'LAT', 'LONG'
        ])
        .with_columns(pl.col(pl.String).str.strip_chars())
        .with_columns(
            pl.col('amphure_th').str.strip_prefix('เขต').alias('amphure_th'),
            pl.col('amphure_en').str.strip_prefix('Khet ').alias('amphure_en'),
        )
        .with_columns(pl.col(pl.String).str.strip_chars())
        .unique()
        .sort(['province_code', 'amphure_code', 'district_code'])
    )
    print(joined_df.head().select('amphure_th', 'amphure_en', 'province_code'))
    joined_df.write_parquet(base_path / '../src/thai_address/data.parquet')

if __name__ == '__main__':
    main()
