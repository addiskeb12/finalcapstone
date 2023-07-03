
import spacy
nlp = spacy.load('en_core_web_sm')
garden_path_sentence = """A research paper published by Meseguer, Carreiras and Clifton (2002) 
stated that intensive eye movements are observed when people are recovering from a mild garden-path sentence. 
They proposed that people use two strategies, both of which are consistent with the selective reanalysis process 
described by Frazier and Rayner in 1982. ",
                        "Mary gave the child a Band-Aid",
                        "That Jill is never here hurts",
                        "The cotton clothing is made of grows in Mississippi"""
nlp_garden_path_sentence = nlp(garden_path_sentence)
print([(i, i.label_, i.label) for i in nlp_garden_path_sentence.ents])
print(spacy.explain('ORG'))
print(spacy.explain('CARDINAL'))
# ORG means includes companies, agencies, institutions. Org is a short form of organisation
# CARDINAL another form of numerals that do not fall under another type
# both of them are make sense to me.
