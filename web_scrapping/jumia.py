import requests
from bs4 import BeautifulSoup

def main(link, fname):
    res = requests.get(link)
    page_source = BeautifulSoup(res.text)
    categories = page_source.find_all("div", attrs={"class":"col16 -pvs"})

    #Get item, price, discount and category
    with open(fname, 'w', encoding="utf16") as f:
        f.write("item,price,discount,category\n")
        for cat in categories:
            title = cat.select("div > h2")
            if not title: continue
            else : category = title[0].getText()
            items = cat.find_all(
                    'div', attrs={'class':["name", "prc", "tag _dsct"]}
                )
            if (len(items)%3)==0:
                for i in range(0, len(items), 3):
                    f.write(
                            f"{items[i].getText()},[{items[i+1].getText()}],"
                            f"{items[i+2].getText()},{category}\n"
                        )
            else:
                n = 0
                while n<len(items):
                    if ((n+2)<len(items)) and ('%' in items[n+2].getText()):
                        f.write(
                                f'"{items[n].getText()}","{items[n+1].getText()}",'
                                f'"{items[n+2].getText()}","{category}"\n'
                            )
                        n += 3
                    else:
                        if (n+1)<len(items):
                            f.write(
                                    f'"{items[n].getText()}","{items[n+1].getText()}]",'
                                    f'?,"{category}"\n'
                                )
                            n += 2
                        else:
                            f.write(f'"{items[n].getText()}",?,?,"{category}"\n')
                            n += 1


if __name__ == "__main__":
    main("https://www.jumia.com.ng/", "jumia.csv")
