from bs4 import BeautifulSoup
import requests


response = requests.get("https://allegro.pl/listing?string=one%20piece%20card%20game%20booster")

soup = BeautifulSoup(response.text, 'html.parser')

boosters = soup.find_all('article', class_='mp7g_oh mpof_ki m389_6m m7er_k4 _9c44d_1D3P9')


boosters_data = {}


for booster in boosters:
    booster_name = booster.find("a", class_="mgn2_14 mp0t_0a mgmw_wo mj9z_5r mli8_k4 mqen_m6 l1fas l1igl meqh_en mpof_z0 mqu1_16 m6ax_n4 _6a66d_LPwkT  ").get_text()
    booster_price = booster.find("div", class_="mli8_k4 msa3_z4 mqu1_1 mp0t_ji m9qz_yo mgmw_qw mgn2_27 mgn2_30_s").get_text()
    booster_link = booster.find("a", class_="mgn2_14 mp0t_0a mgmw_wo mj9z_5r mli8_k4 mqen_m6 l1fas l1igl meqh_en mpof_z0 mqu1_16 m6ax_n4 _6a66d_LPwkT  ").get("href")

    boosters_data[booster_name] = (booster_price, booster_link)


print(boosters_data)
