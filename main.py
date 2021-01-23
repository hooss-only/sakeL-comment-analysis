import json

comments = {}

with open("coments.json", "r", encoding='UTF8') as json_file:
    comments = json.load(json_file)

b = 0
for i in range(30001):

    if comments[str(i)]['comment'].startswith("sake L"):
        # print(f"{comments[str(i)]['author']} : {comments[str(i)]['comment']}")
        b = b+1

    elif comments[str(i)]['comment'].startswith("Sake L"):
        # print(f"{comments[str(i)]['author']} : {comments[str(i)]['comment']}")
        b = b+1


print(f"{i}개의 댓글 중 {b}개의 sake L / Sake L 로 시작하는 찬양 글 발견됨")
