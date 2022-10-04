import metadata_utils as mu

records = mu.read_csv("dlxs_full.csv")
marc_lang = mu.read_csv("marc_lang.csv")

lang_rec_doc = []

for entry in records[1:]:
    if "map" in entry[-2]:
        lang_rec = None
        for lang in marc_lang[1:]:
            if "(" in lang[1]:
                if lang[1].split("(")[0] in entry[-1]:
                    lang_rec = lang[0]
                    lang_rec_doc.append([entry[0],entry[-2],lang_rec, lang[1], entry[-1]])
            elif lang[1] in entry[-1]:
                    lang_rec = lang[0]
                    lang_rec_doc.append([entry[0],entry[-2],lang_rec, lang[1], entry[-1]])
            elif lang[1].split("(")[0] in entry[-3]:
                lang_rec = lang[0]
                lang_rec_doc.append([entry[0],entry[-2],lang_rec, lang[1], entry[-3]])
            elif lang[1] in entry[-3]:
                lang_rec = lang[0]
                lang_rec_doc.append([entry[0],entry[-2],lang_rec, lang[1], entry[-3]])
        if not lang_rec:
            lang_rec_doc.append([entry[0],entry[-2],lang_rec, None, entry[-1]])

lang_rec_doc.insert(0, ["mms_id", "alma_lang", "language_reccomendation_marc_code", "marc_lang", "dlxs_tested_value"])
mu.write_csv("map_lang_reccomendations.csv", lang_rec_doc)
print("done")

