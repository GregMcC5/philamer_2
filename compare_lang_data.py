import metadata_utils as mu

dlxs = mu.read_csv("/Users/gregorymccollum/Documents/GitHub/philamer/dif/dlxs_full")
final = mu.read_csv("Subject_Sorting/new_full_best_values.csv")

changes = [["dlxs", "new_lang", "original_lang"]]

for record in final:
    dlxs_original = [x for x in dlxs if x[1] == record[1]]
    if len(dlxs_original) == 1:
        dlxs_original = dlxs_original[0]
        if record[-3].strip() != dlxs_original[-2].split(":")[0].strip("['").strip():
            print(record[-3].strip())
            print(dlxs_original[-2].split(":")[0].strip("['").strip())
            print("\n")
            changes.append([record[1],record[-3],dlxs_original[-2]])
    else:
        print("uh oh")
    
mu.write_csv("lang_changes.csv",changes)