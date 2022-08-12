import re

with open('train') as f:
    lines = f.readlines()


def turkerify(parsed):
    result = ""
    pattern = re.compile(r'(\([^\)]*)?\(([^\(]*?)\s(.*?)\)(\)*)')
    for tag in pattern.finditer(parsed):
        result += f'{tag.group(1) or ""}({tag.group(2)} {isolate_tag(tag.group(2))}{tag.group(4) or ""})'
    return result


def isolate_tag(tag):
    parts = str.split(tag, '-')
    return f'{parts[0]}.{parts[2]}' if len(parts) == 3 else tag

print(turkerify('(ART-NK-Nom.Sg.Fem Die)'))
print(turkerify("(TOP($Par ``)(S-TOP(PN-SB(NE-PNC-Nom.Sg.Masc Ross)(NE-PNC-Nom.Sg.Masc Perot))(VAFIN-HD-3.Sg.Past.Subj w\228re)(ADV-MO vielleicht)(NP-PD(ART-NK-Nom.Sg.Masc ein)(ADJA-NK-Pos.Nom.Sg.Masc pr\228chtiger)(NN-NK-Nom.Sg.Masc Diktator)))($Par ''))"))

add_n = lambda xs : xs + "\n"

newCorpus = map(turkerify, lines)



#f = open("newCorpus.txt", "a")
#f.writelines(map(add_n, newCorpus))
#f.close()


print(turkerify('(TOP(S-TOP($Par ``)(NP-SB(NN-NK-Nom.Sg.Fem Flughöhe)(CARD-NK Null))($Par '')(VVFIN-HD-3.Sg.Pres.Ind macht)(NP-DA(ART-NK-Dat.Sg.Fem der)(NN-NK-Dat.Sg.Fem Industrie))(NN-OA-Acc.Sg.Fem Angst)))'))
print(newCorpus[0])
print(newCorpus[1])

