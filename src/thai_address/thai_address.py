"""Main module."""
import polars as pl
from pathlib import Path
from functools import lru_cache


class ThaiAddress:

    @staticmethod
    @lru_cache()
    def get_address_df() -> pl.DataFrame:
        source = Path(__file__).parent / 'data.parquet'
        return pl.read_parquet(source)

    @staticmethod
    def query_provinces_th(search) -> list[str]:
        df = ThaiAddress.get_address_df()
        return df.select('province_th').unique(maintain_order=True).filter(
            pl.col('province_th').str.contains(search)
        ).to_series().to_list()

    @staticmethod
    def query_amphures_th(search='', province='') -> list[str]:
        df = ThaiAddress.get_address_df()
        if province:
            df = df.filter(
                pl.col('province_th') == province,
            )
        return df.select('amphure_th').unique(maintain_order=True).filter(
            pl.col('amphure_th').str.contains(search),
        ).to_series().to_list()

    @staticmethod
    def query_districts_th(search='', province='', amphure='') -> list[str]:
        df = ThaiAddress.get_address_df()
        if province:
            df = df.filter(
                pl.col('province_th') == province,
            )
        if amphure:
            df = df.filter(
                pl.col('amphure_th') == amphure,
            )
        return df.select('district_th').unique(maintain_order=True).filter(
            pl.col('district_th').str.contains(search)
        ).to_series().to_list()

    @staticmethod
    def query_provinces_en(search) -> list[str]:
        df = ThaiAddress.get_address_df()
        return df.select('province_en').unique(maintain_order=True).filter(
            pl.col('province_en').str.contains(r"(?i)" + search)
        ).to_series().to_list()

    @staticmethod
    def query_amphures_en(search='', province='') -> list[str]:
        df = ThaiAddress.get_address_df()
        if province:
            df = df.filter(
                pl.col('province_en') == province,
            )
        return df.select('amphure_en').unique(maintain_order=True).filter(
            pl.col('amphure_en').str.contains(r"(?i)" + search),
        ).to_series().to_list()

    @staticmethod
    def query_districts_en(search='', province='', amphure='') -> list[str]:
        df = ThaiAddress.get_address_df()
        if province:
            df = df.filter(
                pl.col('province_en') == province,
            )
        if amphure:
            df = df.filter(
                pl.col('amphure_en') == amphure,
            )
        return df.select('district_en').unique(maintain_order=True).filter(
            pl.col('district_en').str.contains(r"(?i)" + search)
        ).to_series().to_list()
