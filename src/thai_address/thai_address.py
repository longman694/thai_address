"""Main module."""
import polars as pl
from pathlib import Path
from functools import lru_cache


class ThaiAddress:

    @staticmethod
    @lru_cache()
    def _load_df():
        source = Path(__file__).parent / 'data.parquet'
        return pl.read_parquet(source)

    @staticmethod
    def query_provinces_th(search):
        df = ThaiAddress._load_df()
        return df.filter(
            pl.col('province_th').str.contains(search)
        ).select('province_th').unique(maintain_order=True).to_series().to_list()

    @staticmethod
    def query_amphures_th(search='', province=''):
        df = ThaiAddress._load_df()
        if province:
            df = df.filter(
                pl.col('province_th') == province,
            )
        return df.filter(
            pl.col('amphure_th').str.contains(search),
        ).select('amphure_th').unique(maintain_order=True).to_series().to_list()

    @staticmethod
    def query_districts_th(search='', province='', amphure=''):
        df = ThaiAddress._load_df()
        if province:
            df = df.filter(
                pl.col('province_th') == province,
            )
        if amphure:
            df = df.filter(
                pl.col('amphure_th') == amphure,
            )
        return df.filter(
            pl.col('district_th').str.contains(search)
        ).select('district_th').unique(maintain_order=True).to_series().to_list()

    @staticmethod
    def query_provinces_en(search):
        df = ThaiAddress._load_df()
        return df.filter(
            pl.col('province_en').str.contains(r"(?i)" + search)
        ).select('province_en').unique(maintain_order=True).to_series().to_list()

    @staticmethod
    def query_amphures_en(search='', province=''):
        df = ThaiAddress._load_df()
        if province:
            df = df.filter(
                pl.col('province_en') == province,
            )
        return df.filter(
            pl.col('amphure_en').str.contains(r"(?i)" + search),
        ).select('amphure_en').unique(maintain_order=True).to_series().to_list()

    @staticmethod
    def query_districts_en(search='', province='', amphure=''):
        df = ThaiAddress._load_df()
        if province:
            df = df.filter(
                pl.col('province_en') == province,
            )
        if amphure:
            df = df.filter(
                pl.col('amphure_en') == amphure,
            )
        return df.filter(
            pl.col('district_en').str.contains(r"(?i)" + search)
        ).select('district_en').unique(maintain_order=True).to_series().to_list()
