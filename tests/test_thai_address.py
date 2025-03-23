#!/usr/bin/env python

"""Tests for `thai_address` package."""

import pytest

from src.thai_address import ThaiAddress


def test_query_provinces_th():
    provinces = ThaiAddress.query_provinces_th('กร')
    assert provinces == ['กรุงเทพมหานคร', 'กระบี่']
    provinces = ThaiAddress.query_provinces_th('บุรี')
    assert provinces == ['นนทบุรี', 'ลพบุรี', 'สิงห์บุรี', 'สระบุรี', 'ชลบุรี', 'จันทบุรี',
                         'ปราจีนบุรี', 'บุรีรัมย์', 'ราชบุรี', 'กาญจนบุรี', 'สุพรรณบุรี', 'เพชรบุรี']


def test_query_provinces_en():
    provinces = ThaiAddress.query_provinces_en('bang')
    assert provinces == ['Bangkok']
    provinces = ThaiAddress.query_provinces_en('buri')
    assert provinces == ['Nonthaburi', 'Lopburi', 'Sing Buri', 'Saraburi', 'Chon Buri',
                         'Chanthaburi', 'Prachin Buri', 'Buri Ram', 'Ratchaburi', 'Kanchanaburi',
                         'Suphan Buri', 'Phetchaburi']


def test_query_amphure_th():
    amphures = ThaiAddress.query_amphures_th('ยาน')
    assert amphures == ['ยานนาวา']
    amphures = ThaiAddress.query_amphures_th('ยาน', province='กรุงเทพมหานคร')
    assert amphures == ['ยานนาวา']
    amphures = ThaiAddress.query_amphures_th(province='กรุงเทพมหานคร')
    assert len(amphures) == 50
    amphures = ThaiAddress.query_amphures_th('', province='ชลบุรี')
    assert amphures == ['เมืองชลบุรี', 'บ้านบึง', 'หนองใหญ่', 'บางละมุง', 'พานทอง', 'พนัสนิคม',
                       'ศรีราชา', 'เกาะสีชัง', 'สัตหีบ', 'บ่อทอง', 'เกาะจันทร์']
    amphures = ThaiAddress.query_amphures_th('ยาน', province='ชลบุรี')
    assert amphures == []


def test_query_amphure_en():
    amphures = ThaiAddress.query_amphures_en('yan nawa')
    assert amphures == ['Yan Nawa']
    amphures = ThaiAddress.query_amphures_en('yan', province='Bangkok')
    assert amphures == ['Yan Nawa']
    amphures = ThaiAddress.query_amphures_en(province='Bangkok')
    assert len(amphures) == 50
    amphures = ThaiAddress.query_amphures_en('', province='Chon Buri')
    assert amphures == ['Mueang Chon Buri', 'Ban Bueng', 'Nong Yai', 'Bang Lamung',
                       'Phan Thong', 'Phanat Nikhom', 'Si Racha', 'Ko Sichang',
                       'Sattahip', 'Bo Thong', 'Ko Chan']
    amphures = ThaiAddress.query_amphures_en('Yann', province='Chon Buri')
    assert amphures == []


def test_query_distinct_th():
    districts = ThaiAddress.query_districts_th('ช่อง')
    assert districts == ['ช่องนนทรี', 'ช่องสาริกา', 'ช่องกุ่ม', 'ปากช่อง', 'ช่องแมว',
                         'ช่องเม็ก', 'ช่องสามหมอ', 'ช่องแค', 'ช่องลม', 'ช่องแคบ',
                         'ช่องสะเดา', 'ช่องด่าน', 'ช่องสะแก', 'ช่องไม้แก้ว', 'ช่อง']
    districts = ThaiAddress.query_districts_th('ช่อง', province='กรุงเทพมหานคร')
    assert districts == ['ช่องนนทรี']
    districts = ThaiAddress.query_districts_th('ช่อง', province='กรุงเทพมหานคร', amphure='ยานนาวา')
    assert districts == ['ช่องนนทรี']
    districts = ThaiAddress.query_districts_th('ช่อง', province='กรุงเทพมหานคร', amphure='บางรัก')
    assert districts == []
    districts = ThaiAddress.query_districts_th(province='กรุงเทพมหานคร')
    assert len(districts) == 152  # should be 184?
    districts = ThaiAddress.query_districts_th('', province='ชลบุรี', amphure='เมืองชลบุรี')
    assert districts == ['บางปลาสร้อย', 'มะขามหย่ง', 'บ้านโขด', 'แสนสุข', 'บ้านสวน', 'หนองรี', 'นาป่า',
                         'หนองข้างคอก', 'ดอนหัวฬ่อ', 'หนองไม้แดง', 'บางทราย', 'คลองตำหรุ', 'เหมือง',
                         'บ้านปึก', 'ห้วยกะปิ', 'เสม็ด', 'อ่างศิลา', 'สำนักบก']
    districts = ThaiAddress.query_districts_th('ช่อง', province='ชลบุรี')
    assert districts == []


def test_query_distinct_en():
    districts = ThaiAddress.query_districts_en('Chong')
    assert districts == ['Chong Nonsi', 'Chong Sarika', 'Na Chong', 'Chong Kum', 'Pak Chong', 'Chong Maeo',
                         'Ta Chong', 'Chong Mek', 'Chong Sam Mo', 'Mon Chong', 'Chong Kham', 'Chong Khae', 'Chong Lom',
                         'Chong Khaep', 'Khlong Krachong', 'Khan Chong', 'Chong Sadao', 'Chong Dan',
                         'Chong Sakae', 'Chong Mai Kaeo', 'Chong', 'Chong Thanon']
    districts = ThaiAddress.query_districts_en('Chong', province='Bangkok')
    assert districts == ['Chong Nonsi']
    districts = ThaiAddress.query_districts_en('Chong', province='Bangkok', amphure='Yan Nawa')
    assert districts == ['Chong Nonsi']
    districts = ThaiAddress.query_districts_en('Chong', province='Bangkok', amphure='Bang Rak')
    assert districts == []
    districts = ThaiAddress.query_districts_en(province='Bangkok')
    assert len(districts) == 152  # should be 184?
    districts = ThaiAddress.query_districts_en('', province='Chon Buri', amphure='Mueang Chon Buri')
    assert districts == ['Bang Pla Soi', 'Makham Yong', 'Ban Khot', 'Saen Suk', 'Ban Suan', 'Nong Ri',
                         'Na Pa', 'Nong Khang Khok', 'Don Hua Lo', 'Nong Mai Daeng', 'Bang Sai', 'Khlong Tamru',
                         'Mueang', 'Ban Puek', 'Huai Kapi', 'Samet', 'Ang Sila', 'Samnak Bok']

    districts = ThaiAddress.query_districts_en('Chong', province='Chon Buri')
    assert districts == []
