import metadata_utils as mu

OR_full = mu.read_csv("OR_lang.csv")
full_best = mu.read_csv("new_full_best_values.csv")

for full_entry in full_best[1:]:
    for OR_entry in OR_full[1:]:
        if full_entry[0] == OR_entry[0]:
            if full_entry[7] != OR_entry[7]:
                full_entry[7] = OR_entry[7]

mu.write_csv("updated_full_best.csv", full_best)