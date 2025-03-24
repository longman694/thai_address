============
Thai Address
============


.. image:: https://img.shields.io/pypi/v/thai_address.svg
        :target: https://pypi.python.org/pypi/thai_address

.. image:: https://img.shields.io/travis/longman694/thai_address.svg
        :target: https://travis-ci.com/longman694/thai_address

.. image:: https://readthedocs.org/projects/thai-address/badge/?version=latest
        :target: https://thai-address.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A Python package for querying Thai provinces (จังหวัด), amphures (อำเภอ), and districts (ตำบล) with ease.


* Free software: MIT license
* Documentation: https://thai-address.readthedocs.io.


Features
--------

* Extreme fast query with polars
* Support both Thai and English


Installation
------------

.. code-block:: bash

    pip install git+https://github.com/longman694/thai_address.git


Usage
-----

Thai

.. code-block:: python

    >>> from thai_address import ThaiAddress
    >>> ThaiAddress.query_provinces_th('สมุทร')

    ['สมุทรปราการ', 'สมุทรสาคร', 'สมุทรสงคราม']

    >>> ThaiAddress.query_amphures_th(province='สมุทรปราการ')

    ['เมืองสมุทรปราการ', 'บางบ่อ', 'บางพลี', 'พระประแดง', 'พระสมุทรเจดีย์', 'บางเสาธง']

    >>> ThaiAddress.query_amphures_th('พระ', province='สมุทรปราการ')

    ['พระประแดง', 'พระสมุทรเจดีย์']

    >>> ThaiAddress.query_districts_th(province='สมุทรปราการ', amphure='พระสมุทรเจดีย์')

    ['นาเกลือ', 'บ้านคลองสวน', 'แหลมฟ้าผ่า', 'ปากคลองบางปลากด', 'ในคลองบางปลากด']

    >>> ThaiAddress.query_districts_th('บา', province='สมุทรปราการ', amphure='พระสมุทรเจดีย์')

    ['ปากคลองบางปลากด', 'ในคลองบางปลากด']

    >>> ThaiAddress.get_zip_code_th('ชลบุรี', 'เมืองชลบุรี', 'อ่างศิลา')

    [20000]

English

.. code-block:: python

    >>> from thai_address import ThaiAddress
    >>> ThaiAddress.query_provinces_en('Samut')

    ['Samut Prakan', 'Samut Sakhon', 'Samut Songkhram']

    >>> ThaiAddress.query_amphures_en('pra', province='Samut Prakan')

    ['Phra Pradaeng', 'Phra Samut Chedi']

    >>> ThaiAddress.query_districts_en('ba', province='Samut Prakan', amphure='Phra Samut Chedi')

    ['Ban Khlong Suan', 'Pak Klong Bang Pla Kot', 'Nai Khlong Bang Pla Kot']

    >>>  ThaiAddress.get_zip_code_en('Chon Buri', 'Mueang Chon Buri', 'Ang Sila')

    [20000]

Get full table

.. code-block:: python

    >>> from thai_address import ThaiAddress
    >>> ThaiAddress.get_address_df().head()
    shape: (5, 12)
    ┌───────────────┬────────────────┬────────────────────────────┬──────────────┬───┬─────────────┬──────────┬────────┬─────────┐
    │ district_code ┆ district_th    ┆ district_en                ┆ amphure_code ┆ … ┆ province_en ┆ zip_code ┆ LAT    ┆ LONG    │
    │ ---           ┆ ---            ┆ ---                        ┆ ---          ┆   ┆ ---         ┆ ---      ┆ ---    ┆ ---     │
    │ i32           ┆ str            ┆ str                        ┆ i32          ┆   ┆ str         ┆ i32      ┆ f64    ┆ f64     │
    ╞═══════════════╪════════════════╪════════════════════════════╪══════════════╪═══╪═════════════╪══════════╪════════╪═════════╡
    │ 100101        ┆ พระบรมมหาราชวัง ┆ Phra Borom Maha Ratchawang ┆ 1001         ┆ … ┆ Bangkok     ┆ 10200    ┆ 13.751 ┆ 100.492 │
    │ 100102        ┆ วังบูรพาภิรมย์     ┆ Wang Burapha Phirom        ┆ 1001         ┆ … ┆ Bangkok     ┆ 10200    ┆ 13.744 ┆ 100.499 │
    │ 100103        ┆ วัดราชบพิธ       ┆ Wat Ratchabophit           ┆ 1001         ┆ … ┆ Bangkok     ┆ 10200    ┆ 13.75  ┆ 100.499 │
    │ 100104        ┆ สำราญราษฎร์     ┆ Samran Rat                 ┆ 1001         ┆ … ┆ Bangkok     ┆ 10200    ┆ 13.751 ┆ 100.503 │
    │ 100105        ┆ ศาลเจ้าพ่อเสือ    ┆ San Chao Pho Suea          ┆ 1001         ┆ … ┆ Bangkok     ┆ 10200    ┆ 13.754 ┆ 100.497 │
    └───────────────┴────────────────┴────────────────────────────┴──────────────┴───┴─────────────┴──────────┴────────┴─────────┘

Credits
-------

- Powered by Polars_
- This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Polars: https://pola.rs/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
