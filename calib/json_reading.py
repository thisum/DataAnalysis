import json


with open('train.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

for para in data:
    print(para["title"])

    for p in para["paragraphs"]:
        print(p["context"])

        for qas in p["qas"]:
            print(qas["id"])
            print(qas["question"])

            #for the test file, "answer" is a json object, so can be read as follows. but for train file, it's a json array, hence has to use the for loop
            print(qas["answer"])

            #use only for training file
            # for text in qas["answer"]:
            #     print(text["text"])
            #     print(text["answer_start"])
