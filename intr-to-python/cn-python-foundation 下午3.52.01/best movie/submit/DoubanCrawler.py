import expanddouban
from bs4 import BeautifulSoup
import csv
import codecs

# 定义getMovieUrl函数，参数为电影分类和地区，输出符合该条件的url链接
def getMovieUrl(category, location):
    """
    return a string corresponding to the URL of douban movie lists given category and location.
    """
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    resultUrl = url + ',' + category + ',' + location
    return resultUrl

#定义一个电影类和实现构造函数
class Movie:
    """docstring for Movie."""
    def __init__(self, name,rate,location,category,info_link,cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link
    def print_data(self):
        return [self.name,self.rate,self.location,self.category,self.info_link,self.cover_link]

def getMovies(category,location):
    """
    return a list of Movie objects with the given category and location.
    """
    movies = []
    for loc in location:
        html = expanddouban.getHtml(getMovieUrl(category,loc))
        soup = BeautifulSoup(html,'html.parser')
        content_a = soup.find(id='content').find(class_='list-wp').find_all('a',recursive=False)
        for element in content_a:
            M_name = element.find(class_='title').string
            M_rate = element.find(class_='rate').string
            M_location = loc
            M_category = category
            M_info_link = element.get('href')
            M_cover_link = element.find('img').get('src')
            movies.append(Movie(M_name,M_rate,M_location,M_category,M_info_link,M_cover_link).print_data())
            # movies.append([M_name, M_rate, M_location, M_category, M_info_link, M_cover_link])
    return movies

category_list =['剧情','恐怖','暴力']
location_list = ['大陆','美国','香港']
movies_list = []
for cate in category_list:
    movies_list.extend(getMovies(cate,location_list))

with open('movies.csv', 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    for element in movies_list:
        writer.writerow(element)
# location_list = ['大陆','美国','香港','台湾','日本','韩国','英国','法国','德国','意大利','西班牙',
# '印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦']

# my_list1 = getMovies('黑色幽默',location_list)
# my_list2 = getMovies('恐怖',location_list)
# my_list3 = getMovies('暴力',location_list)
#
# # 选择三个类别获取电影信息列表，将列表信息输出到文件movies.csv
# f = codecs.open('movies.csv', 'w', 'utf_8_sig')
# writer = csv.writer(f)
# writer.writerow(my_list1)
# writer.writerow(my_list2)
# writer.writerow(my_list3)
# f.close()
# movies_list = []
# fcsv = codecs.open('movies.csv', 'w', 'utf_8_sig')
# csv_writer = csv.writer(fcsv)
# for cat in category_list:
#     movies_list = (getMovies(cat,location_list))
#     for movie in movies_list:
#         csv_writer.writerow([movie.name, movie.rate, movie.location, movie.category, movie.info_link, movie.cover_link])
# fcsv.close()


# with open('movies.csv', 'w', encoding= 'utf-8-sig') as f:
# 	writer = csv.writer(f)
# 	for row in movies_list:
# 		writer.writerow(row)

# 将三种类别的电影列表进行排序，输出数量排名前三的地区和分别占有的百分比，输出到output.txt
# def putMax(mylist):
#     input_dict = {'大陆':0,'美国':0,'香港':0,'台湾':0,'日本':0,'韩国':0,'英国':0,'法国':0,'德国':0,'意大利':0,'西班牙':0,
#     '印度':0,'泰国':0,'俄罗斯':0,'伊朗':0,'加拿大':0,'澳大利亚':0,'爱尔兰':0,'瑞典':0,'巴西':0,'丹麦':0}
#     total = 0
#     for movie in mylist:
#         for loc in location_list:
#             if loc in movie:
#                 input_dict[loc] += 1
#                 total += 1
#     for idict in input_dict:
#         input_dict[idict] = round((input_dict[idict]/total)*100,2)
#     return sorted(input_dict.items(), key=lambda x:x[1],reverse=True)[:3]
#
# def turnTostr(max_tuple):
#     result_list = []
#     i = 0
#     while i < len(max_tuple):
#         element = max_tuple[i]
#         ele = str(element)
#         e = "{}占百分之{},排名第{}".format(ele[2:ele.index(',') - 1],ele[ele.index(',') + 2:-3],i + 1)
#         i += 1
#         result_list.append(e)
#     return result_list
#
# max_list = [turnTostr(putMax(my_list1)),turnTostr(putMax(my_list2)),turnTostr(putMax(my_list3))]
#
# f = open('output.txt', 'w')
# f.write("先说好，我选择这几个类型不是我真的喜欢，只是因为数据少，哈哈哈！\n")
# j = 0
# while j < len(category_list):
#     f.write("{}类别电影数量排名前三的地区和百分比为：\n".format(category_list[j]))
#     i = 0
#     while i < len(max_list[j]):
#         f.write(max_list[j][i])
#         f.write('\n')
#         i += 1
#     j += 1
#
# f.close()
