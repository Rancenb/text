import requests
from bs4 import BeautifulSoup

#get函数得到数据并设置requests的请求头.
headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"}
# 发起GET请求并获取网页内容
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
response = requests.get(url)
if response.status_code != 200:
    raise Exception()
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, "html.parser")

# 查找筛选条件的下拉列表
bond_type_select = soup.find("select", attrs={"name": "bondType"})
issue_year_select = soup.find("select", attrs={"name": "instYear"})

# 获取筛选条件的选项值
bond_type_options = [option["value"] for option in bond_type_select.find_all("option")]
issue_year_options = [option["value"] for option in issue_year_select.find_all("option")]

# 设置筛选条件为Treasury Bond和2023
selected_bond_type = "Treasury Bond"
selected_issue_year = "2023"

# 检查筛选条件的选项值是否存在于下拉列表中
if selected_bond_type not in bond_type_options:
    print(f"Invalid bond type: {selected_bond_type}")
    exit()
if selected_issue_year not in issue_year_options:
    print(f"Invalid issue year: {selected_issue_year}")
    exit()

# 发起POST请求以应用筛选条件
payload = {
    "bondType": selected_bond_type,
    "instYear": selected_issue_year
}
response = requests.post(url, data=payload)
html_content = response.text

# 使用BeautifulSoup解析筛选后的网页内容
soup = BeautifulSoup(html_content, "html.parser")

# 查找数据所在的HTML元素
data_table = soup.find("table", class_="data_table")
table_rows = data_table.find_all("tr")

# 打印列名
header_row = table_rows[0]
header_cells = header_row.find_all("th")
column_names = [cell.get_text(strip=True) for cell in header_cells]
print("  ".join(column_names))

# 提取符合条件的数据并打印
for row in table_rows[1:]:
    cells = row.find_all("td")
    if len(cells) == len(column_names):
        data = [cell.get_text(strip=True) for cell in cells]
        print("  ".join(data))