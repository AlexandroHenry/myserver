from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId
from django.http import HttpResponse, JsonResponse
import pymongo
import numpy as np

client = pymongo.MongoClient('mongodb+srv://alaxhenry:Tmdcjdahzk123@alaxhenry.3bowh.mongodb.net/?retryWrites=true&w=majority')
db = client['Bible']
krv = db["KRV"]
KRV_Baptism = db["KRV_BAPTISM"]
niv = db["NIV"]
kjv = db["KJV"]
nkjv = db["NKJV"]
cuv = db["CHIUNL"]

@csrf_exempt
def testAPI(requests):

    person = {'name': 'Dennis', 'age': 28}
    return JsonResponse(person)

# path("readbible/<str:book>&chapter=<int:chapter>/version=<str:version>&language=<str:language>", readbibleChapter)
@csrf_exempt
def readbibleChapter(request, book, chapter, version):
    print(f"book: {book}, chapter: {chapter}, version: {version}")

    reference = f"{book} {chapter}"
    verses = []
    
    wholeText = ""
    translation_id = ""
    translation_name = ""
    translation_note = ""

    if version == "krv":
        translation_id = "krv"
        translation_name = "Korean Revised Version"

        datas = list(krv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        }))

        count = krv.count_documents({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        })
    
    if version == "krv_baptism":
        translation_id = "krvb"
        translation_name = "Korean Revised Version: Baptism"

        datas = list(KRV_Baptism.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        }))

        count = KRV_Baptism.count_documents({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        })

    if version == "niv":
        translation_id = "niv"
        translation_name = "New International Version"

        datas = list(niv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        }))

        count = niv.count_documents({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        })
        translation_id = "niv"
        translation_name = "New International Version"
    
    if version == "kjv":
        translation_id = "kjv"
        translation_name = "King James Version"

        datas = list(kjv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        }))

        count = kjv.count_documents({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        })

    if version == "nkjv":
        translation_id = "kjv"
        translation_name = "King James Version"

        datas = list(nkjv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        }))

        count = nkjv.count_documents({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        })

    if version == "cuv":
        translation_id = "cuv"
        translation_name = "Chinese Union Version"

        datas = list(cuv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        }))

        count = cuv.count_documents({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter}
        })

    for i in range(count):
        book_id = datas[i]["book_id"]
        book_name = datas[i]["book_name"]
        verse = datas[i]["verse"]
        text = datas[i]["text"]

        data = {
            "book_id": book_id, 
            "book_name": book_name,
            "chapter": chapter,
            "verse": verse,
            "text": text
            }

        verses.append(data)

        wholeText += f"{text}\n"

    data = {
        "reference": reference,
        "verses": verses,
        "text": wholeText,
        "translation_id": translation_id,
        "translation_name": translation_name
    }

    return JsonResponse(data)

@csrf_exempt
def readbibleVerse(request, book, chapter, verse, version):
    print(f"book: {book}, chapter: {chapter}, verse: {verse}, version: {version}")
    
    reference = f"{book} {chapter}:{verse}"

    wholeText = ""
    translation_id = ""
    translation_name = ""
    translation_note = ""

    verses = []

    if version == "krv":
        datas = krv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter},
            "verse": {"$eq": verse},
        })
        translation_id = "krv"
        translation_name = "Korean Revised Version"

    if version == "krv_baptism":
        datas = KRV_Baptism.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter},
            "verse": {"$eq": verse},
        })
        translation_id = "krvb"
        translation_name = "Korean Revised Version: Baptism"

    if version == "niv":
        datas = niv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter},
            "verse": {"$eq": verse},
        })
        translation_id = "niv"
        translation_name = "New International Version"

    if version == "kjv":
        datas = kjv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter},
            "verse": {"$eq": verse},
        })
        translation_id = "kjv"
        translation_name = "King James Version"

    if version == "nkjv":
        datas = nkjv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter},
            "verse": {"$eq": verse},
        })
        translation_id = "kjv"
        translation_name = "King James Version"

    if version == "cuv":
        datas = cuv.find({
            "book_name": {"$eq": book},
            "chapter": {"$eq": chapter},
            "verse": {"$eq": verse},
        })
        translation_id = "cuv"
        translation_name = "Chinese Union Version"

    wholeText = datas[0]["text"]
    
    data = {
            "book_id": datas[0]["book_id"], 
            "book_name": datas[0]["book_name"],
            "chapter": chapter,
            "verse": verse,
            "text": datas[0]["text"]
            }

    verses.append(data)

    data = {
        "reference": reference,
        "verses": verses,
        "text": wholeText,
        "translation_id": translation_id,
        "translation_name": translation_name
    }
    

    return JsonResponse(data)