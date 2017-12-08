'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2015.
'''

import math
import re

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    len1 = 0
    len2 = 0
    dot_product=0
    for k1,v1 in vec1.items():
        if k1 in vec2.keys():
            dot_product+=vec1[k1]*vec2[k1]
        len1+=v1**2
    for k2,v2 in vec2.items():
        len2+=v2**2
    return dot_product/(len1*len2)**0.5


def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d:
                d[word]={}

    for sentence in sentences:
        for word in sentence:
            other_words = list(sentence)
            while word in other_words:
                other_words.remove(word)
            for others in other_words:
                if word not in d[others]:
                    d[others][word]=1
                else:
                    d[others][word]+=1
    return d
                

def build_semantic_descriptors_from_files(filenames):
    test=open('Tolstoy.txt','r',encoding = 'utf-8')
    lines = (''.join(test.readlines())).lower()
    lines = lines.replace('\n',' ')
    lines = lines.replace('"','')
    lines = lines.replace('\'','')
    sentences=(re.split( r',|\.|\!|\?', lines))
    load = []
    for sentence in sentences:
        sen = sentence.split()
        load.append(sen)
    d = build_semantic_descriptors(load)
    return d





def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    sim_word=''
    sim=0
    for c in choices:
        temp_sim = similarity_fn(semantic_descriptors[word],semantic_descriptors[c])
        if temp_sim>sim:
            sim=float(temp_sim)
            sim_word = c
    return sim_word


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    

    test = open(test.txt,'r')
    correct =0
    line = test.readline()
    while line!='EOF':
        tests+=1
        ls = line.split()
        word = ls[0]
        answer = ls[1]
        choices = ls[2:]
        if most_similar_word(word,choices,semantic_descriptors,similarity_fn)==answer:
            correct +=1
        line = test.readline()
        print(correct/tests)


def main():

    '''sen=[['i','am','a','person'],['i','am','also','a','human']]
    
    d=build_semantic_descriptors(sen)
    for key in d:
        print(key,d[key])'''
    #start = time.time()
    build_semantic_descriptors_from_files(['Proust.txt','Tolstoy.txt'])
    #end = time.time()
    #print(end-start)


main()
