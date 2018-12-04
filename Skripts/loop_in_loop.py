import requests
#
# urlik = "http://leroymerlin.ru/api/v2/"
# urlik_test = "https://m5-43.lm.greensight.ru/api/v2/"
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# headers_test = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization':
#     'Basic Z3JlZW5zaWdodDpncmVlbnNpZ2h0'}
#
# data = {'entity':'categories', 'idShop':72, 'getSA':1}
#
# categories_list = requests.post(urlik, data=data, headers=headers, verify=False)
#
# categories_list_json = categories_list.json()
#
# name_categories = categories_list_json[0]["childs"][0]["childs"][1]["name"]
# print(name_categories)
#
# list_name_categories = []
#
# for (_, item) in enumerate(categories_list_json):
#     for (_, subitem) in enumerate(item["childs"]):
#         for (_, subsubitem) in enumerate(subitem["childs"]):
#             # for (_, subsubsubitem) in enumerate(subsubitem["catid"]):
#             for (_, subsubitem) in enumerate['parentId']:
#                 # list_name_categories.append(subsubsubitem)
#                 #
#                 # for (_, subsubsubsubitem) in enumerate(subsubsubitem):
#                 #     for (_, subsubsubsubsubitem) in enumerate(subsubsubsubitem["name"]):  list_name_categories.append(subsubsubitem)
#
# # print(list_name_categories














import requests

urlik = "http://leroymerlin.ru/api/v2/"
urlik_test = "https://m5-43.lm.greensight.ru/api/v2/"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
headers_test = {'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic Z3JlZW5zaWdodDpncmVlbnNpZ2h0'}

data = {'entity': 'projects_tags', 'action': 'getTags'}

project_list = requests.post(urlik, data=data, headers=headers, verify=False)

# print(project_list.status_code)

project_list_json = project_list.json()

# print(project_list_json)

print(project_list.status_code)
project_list_json[0]['tags'][0]
print(project_list_json[0]['tags'][0])
a = []
# print(project_list_json[0]['tags'][0]['tag_projects'])

for (_, item) in enumerate(project_list_json):
    for (_, subitem) in enumerate(item['tags']):
        for (_, subsubitem) in enumerate(subitem['tag_projects']):
            a.append(subsubitem)

print(a)